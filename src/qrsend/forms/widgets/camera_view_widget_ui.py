from qrsend.dirs import application_dir
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_view_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CameraViewWidget(object):
    def setupUi(self, CameraViewWidget):
        if not CameraViewWidget.objectName():
            CameraViewWidget.setObjectName(u"CameraViewWidget")
        CameraViewWidget.resize(544, 275)
        self.horizontalLayout = QHBoxLayout(CameraViewWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gvw_main = QGraphicsView(CameraViewWidget)
        self.gvw_main.setObjectName(u"gvw_main")

        self.horizontalLayout.addWidget(self.gvw_main)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_to_qr = QPushButton(CameraViewWidget)
        self.btn_to_qr.setObjectName(u"btn_to_qr")

        self.verticalLayout.addWidget(self.btn_to_qr)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(CameraViewWidget)

        QMetaObject.connectSlotsByName(CameraViewWidget)
    # setupUi

    def retranslateUi(self, CameraViewWidget):
        CameraViewWidget.setWindowTitle(QCoreApplication.translate("CameraViewWidget", u"Form", None))
        self.btn_to_qr.setText(QCoreApplication.translate("CameraViewWidget", u"Back to QR", None))
    # retranslateUi

