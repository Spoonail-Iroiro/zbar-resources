from qrsend.dirs import application_dir
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qr_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_QRWidget(object):
    def setupUi(self, QRWidget):
        if not QRWidget.objectName():
            QRWidget.setObjectName(u"QRWidget")
        QRWidget.resize(560, 300)
        self.horizontalLayout = QHBoxLayout(QRWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gvw_main = QGraphicsView(QRWidget)
        self.gvw_main.setObjectName(u"gvw_main")

        self.horizontalLayout.addWidget(self.gvw_main)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chk_enable = QCheckBox(QRWidget)
        self.chk_enable.setObjectName(u"chk_enable")

        self.verticalLayout.addWidget(self.chk_enable)

        self.btn_to_camera = QPushButton(QRWidget)
        self.btn_to_camera.setObjectName(u"btn_to_camera")

        self.verticalLayout.addWidget(self.btn_to_camera)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(QRWidget)

        QMetaObject.connectSlotsByName(QRWidget)
    # setupUi

    def retranslateUi(self, QRWidget):
        QRWidget.setWindowTitle(QCoreApplication.translate("QRWidget", u"Form", None))
        self.chk_enable.setText(QCoreApplication.translate("QRWidget", u"Enable", None))
        self.btn_to_camera.setText(QCoreApplication.translate("QRWidget", u"Disable and \n"
"go to camera", None))
    # retranslateUi

