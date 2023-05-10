from PySide6.QtWidgets import QDialog, QWidget, QMainWindow, QFileDialog
from pathlib import Path
from PIL import Image, ImageDraw
from typing import Optional, List, Tuple
from PySide6.QtCore import QTimer
from .main_form_ui import Ui_MainForm
from .widgets.qr_widget import QRWidget
from .widgets.camera_view_widget import CameraViewWidget
from ..core.camera import get_camera
from ..core.data_receiver import DataReceiver, ChecksumError, SameChecksum
from ..core.data_sender import DataSender
from ..core.qr import decode_first_qr
import cv2
from enum import Enum, auto
import qrcode
import qrcode.util
import logging
logger = logging.getLogger(__name__)

class ClientMode(Enum):
    SEND = auto()
    RECIEVE = auto()


class MainForm(QMainWindow):
    def __init__(self, client_mode: ClientMode, send_qr_version: Optional[int] = None, send_byte_limit=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        # sendかreceiveか
        self.client_mode = client_mode

        if client_mode == ClientMode.SEND and (send_qr_version is None or send_byte_limit is None):
            raise ValueError(f"Sepcify QR version and byte length limit for send")

        if client_mode == ClientMode.SEND:
            self.setWindowTitle(f"Send")
        else:
            self.setWindowTitle(f"Receive")

        # 送信時QRコードバージョン
        self.send_qr_version = send_qr_version
        self.send_byte_limit = send_byte_limit

        # StackedWidgetsの設定 QR表示画面とカメラ確認画面
        self.qr_widget = QRWidget(self)
        self.camera_view_widget = CameraViewWidget(self)
        self.widgets = [
            self.qr_widget,
            self.camera_view_widget
        ]
        for wid in self.widgets:
            self.ui.stw_main.addWidget(wid)
        self.ui.stw_main.setCurrentIndex(0)

        # VideoCaptureを取得
        self.capture = get_camera()

        # 最初のupdate+以降30FPSでカメラ更新
        self.update_camera()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(34)

        self.data_sender: Optional[DataSender] = None
        self.data_receiver: Optional[DataReceiver] = None

        if self.client_mode == ClientMode.RECIEVE:
            self.data_receiver = DataReceiver()

        # self.camera_view_widget.ui.pushButton.clicked.connect(self.update_camera)

        self.qr_widget.ui.btn_to_camera.clicked.connect(self.on_go_to_camera)
        self.camera_view_widget.ui.btn_to_qr.clicked.connect(self.on_go_to_qr)
        self.ui.btn_file.clicked.connect(self.on_btn_file_clicked)

    def on_btn_file_clicked(self):
        if self.client_mode == ClientMode.SEND:
            path_str, _ = QFileDialog.getOpenFileName(self)
            if path_str != "":
                path = Path(path_str)
                self.data_sender = DataSender(path.read_bytes(), self.send_byte_limit)
                self._set_send_data()
                self.ui.lbl_read_value.setText(f"{path}")

        elif self.client_mode == ClientMode.RECIEVE:
            path_str, _ = QFileDialog.getSaveFileName(self)
            if path_str != "":
                path = Path(path_str)
                data = self.data_receiver.get_stored()
                path.write_bytes(data)
                self.ui.lbl_file.setText(f"受信データをセーブしました：{path}")

        pass

    def on_go_to_camera(self):
        self.qr_widget.ui.chk_enable.setChecked(False)
        self.ui.stw_main.setCurrentIndex(1)

    def on_go_to_qr(self):
        self.ui.stw_main.setCurrentIndex(0)

    def update_camera(self):
        ret, frame = self.capture.read()
        if not ret:
            raise ValueError(f"Getting frame failed")

        grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        self.camera_view_widget.set_pic(grayed)

        if self.qr_widget.ui.chk_enable.isChecked():
            if self.client_mode == ClientMode.SEND and self.data_sender is not None:
                decoded = decode_first_qr(grayed)
                if decoded is not None:
                    if self.data_sender.confirm(decoded):
                        self.ui.txt_read_value.setText(f"検出成功：{decoded}")
                        logger.info(f"送信成功：{decoded}")
                        # 次のデータにupdateしてから新たなQRをセット
                        is_updated = self.data_sender.update()
                        if is_updated:
                            self._set_send_data()
                        else:
                            self.qr_widget.ui.chk_enable.setChecked(False)
                            self.ui.txt_read_value.setText(f"検出終了")
                    else:
                        self.ui.txt_read_value.setText(f"検出成功/検証失敗：{decoded}")
            elif self.client_mode == ClientMode.RECIEVE and self.data_receiver is not None:
                decoded = decode_first_qr(grayed)
                if decoded is not None:
                    try:
                        sum = self.data_receiver.receive(decoded)
                        # 受け取ったチェックサムデータをQRで表示
                        self._set_received_sum(sum)
                        self.ui.txt_read_value.setText(f"検出成功：{sum}")
                        logger.info(f"受信成功：{sum}")
                    except ChecksumError as ce:
                        self.ui.txt_read_value.setText(f"検出成功/検証失敗：{ce}")
                        logger.warning(f"検出成功/検証失敗：{ce}")
                    except SameChecksum as sce:
                        pass


    def _data_to_qr(self, data: bytes, version=None) -> Image.Image:
        qrdata = qrcode.util.QRData(data)
        if version is None:
            version = self.send_qr_version
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )
        qr.add_data(qrdata)
        qr.make(fit=False)

        img = qr.make_image()
        image = img._img

        return image

    def _set_send_data(self):
        data_send = self.data_sender.send()
        qr_image = self._data_to_qr(data_send)
        self.qr_widget.set_pic(qr_image)

    def _set_received_sum(self, sum):
        qr_image = self._data_to_qr(sum, 1)
        self.qr_widget.set_pic(qr_image)

    def resizeEvent(self, event) -> None:
        self.qr_widget.on_resize()
        self.camera_view_widget.on_resize()
