from PySide6.QtWidgets import QDialog, QWidget, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from .camera_view_widget_ui import Ui_CameraViewWidget
import logging
logger = logging.getLogger(__name__)


class CameraViewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CameraViewWidget()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        gvw = self.ui.gvw_main
        gvw.setScene(self.scene)
        # gvw.setSceneRect(0,0,gvw.frameRect().width(),gvw.frameRect().height())

    def set_pic(self, cv_mat):
        h, w = cv_mat.shape[:2]
        image = QImage(cv_mat.flatten(), w, h, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image)

        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.on_resize()

    def on_resize(self):
        self.ui.gvw_main.ensureVisible(self.scene.sceneRect())
        self.ui.gvw_main.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
