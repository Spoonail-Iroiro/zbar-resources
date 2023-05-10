from qrsend.dirs import application_dir
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SelectForm(object):
    def setupUi(self, SelectForm):
        if not SelectForm.objectName():
            SelectForm.setObjectName(u"SelectForm")
        SelectForm.resize(213, 64)
        self.horizontalLayout_2 = QHBoxLayout(SelectForm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.btn_send = QPushButton(SelectForm)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout_2.addWidget(self.btn_send)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_receive = QPushButton(SelectForm)
        self.btn_receive.setObjectName(u"btn_receive")

        self.horizontalLayout_2.addWidget(self.btn_receive)


        self.retranslateUi(SelectForm)

        QMetaObject.connectSlotsByName(SelectForm)
    # setupUi

    def retranslateUi(self, SelectForm):
        SelectForm.setWindowTitle(QCoreApplication.translate("SelectForm", u"Dialog", None))
        self.btn_send.setText(QCoreApplication.translate("SelectForm", u"send", None))
        self.btn_receive.setText(QCoreApplication.translate("SelectForm", u"receive", None))
    # retranslateUi

