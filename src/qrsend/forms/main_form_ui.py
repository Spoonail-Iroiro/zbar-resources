from qrsend.dirs import application_dir
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(509, 264)
        self.centralwidget = QWidget(MainForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stw_main = QStackedWidget(self.centralwidget)
        self.stw_main.setObjectName(u"stw_main")

        self.verticalLayout.addWidget(self.stw_main)

        self.lbl_read_value = QLabel(self.centralwidget)
        self.lbl_read_value.setObjectName(u"lbl_read_value")

        self.verticalLayout.addWidget(self.lbl_read_value)

        self.txt_read_value = QLineEdit(self.centralwidget)
        self.txt_read_value.setObjectName(u"txt_read_value")

        self.verticalLayout.addWidget(self.txt_read_value)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_file = QPushButton(self.centralwidget)
        self.btn_file.setObjectName(u"btn_file")

        self.horizontalLayout.addWidget(self.btn_file)

        self.lbl_file = QLabel(self.centralwidget)
        self.lbl_file.setObjectName(u"lbl_file")

        self.horizontalLayout.addWidget(self.lbl_file)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 509, 22))
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainForm)
        self.statusbar.setObjectName(u"statusbar")
        MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"MainWindow", None))
        self.lbl_read_value.setText(QCoreApplication.translate("MainForm", u"\u73fe\u5728\u306e\u8aad\u307f\u53d6\u308a\u5024", None))
        self.btn_file.setText(QCoreApplication.translate("MainForm", u"\u958b\u304f", None))
        self.lbl_file.setText(QCoreApplication.translate("MainForm", u"none", None))
    # retranslateUi

