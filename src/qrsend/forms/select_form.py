from PySide6.QtWidgets import QDialog, QWidget
from .select_form_ui import Ui_SelectForm
from .main_form import MainForm, ClientMode



class SelectForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SelectForm()
        self.ui.setupUi(self)

        self.ui.btn_send.clicked.connect(self.on_btn_send_clicked)
        self.ui.btn_receive.clicked.connect(self.on_btn_receive_clicked)

    def on_btn_send_clicked(self):
        self.form = MainForm(ClientMode.SEND, send_qr_version=22, send_byte_limit=999)
        self.form.show()

    def on_btn_receive_clicked(self):
        self.form = MainForm(ClientMode.RECIEVE)
        self.form.show()
