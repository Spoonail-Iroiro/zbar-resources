from PySide6.QtWidgets import QDialog, QWidget, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PIL import ImageQt
from PySide6.QtCore import Qt
from .qr_widget_ui import Ui_QRWidget


class QRWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QRWidget()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        gvw = self.ui.gvw_main
        gvw.setScene(self.scene)

    def set_pic(self, pil_image):
        image = ImageQt.ImageQt(pil_image)
        pixmap = QPixmap.fromImage(image)

        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.on_resize()

    def on_resize(self):
        self.ui.gvw_main.ensureVisible(self.scene.sceneRect())
        self.ui.gvw_main.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
