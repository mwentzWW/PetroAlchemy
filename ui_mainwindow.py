# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1398, 932)
        font = QFont()
        font.setFamily(u"Cascadia Code")
        main_window.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-rad"
                        "ius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-righ"
                        "t-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargrad"
                        "ient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	"
                        "border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qli"
                        "neargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"	color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, "
                        "x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	border-bot"
                        "tom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlinear"
                        "gradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-le"
                        "ft:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2"
                        ":0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBo"
                        "x {\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), "
                        "stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-style: solid;\n"
"	bord"
                        "er-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTo"
                        "olBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
""
                        "	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
""
                        "	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
""
                        "   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizo"
                        "ntal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"   background: none;\n"
"}")
        self.actionImport_Data = QAction(main_window)
        self.actionImport_Data.setObjectName(u"actionImport_Data")
        self.actionImport_Data.setCheckable(True)
        self.actionImport_Data.setChecked(False)
        icon1 = QIcon()
        icon1.addFile(u"resources/document_exchange_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport_Data.setIcon(icon1)
        self.actionImport_Data.setFont(font)
        self.actionTutorial = QAction(main_window)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionTutorial.setFont(font)
        self.actionSponsor = QAction(main_window)
        self.actionSponsor.setObjectName(u"actionSponsor")
        self.actionSponsor.setFont(font)
        self.actionProject_Website = QAction(main_window)
        self.actionProject_Website.setObjectName(u"actionProject_Website")
        self.actionProject_Website.setFont(font)
        self.actionDocumentation = QAction(main_window)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionDocumentation.setFont(font)
        self.actionWebsite = QAction(main_window)
        self.actionWebsite.setObjectName(u"actionWebsite")
        self.actionWebsite.setFont(font)
        self.actionReport_a_bug = QAction(main_window)
        self.actionReport_a_bug.setObjectName(u"actionReport_a_bug")
        self.actionReport_a_bug.setFont(font)
        self.actionPropose_a_new_feauture = QAction(main_window)
        self.actionPropose_a_new_feauture.setObjectName(u"actionPropose_a_new_feauture")
        self.actionPropose_a_new_feauture.setFont(font)
        self.actionBugs_and_feature_requests = QAction(main_window)
        self.actionBugs_and_feature_requests.setObjectName(u"actionBugs_and_feature_requests")
        self.actionBugs_and_feature_requests.setFont(font)
        self.actionContact_project_creator = QAction(main_window)
        self.actionContact_project_creator.setObjectName(u"actionContact_project_creator")
        self.actionContact_project_creator.setFont(font)
        self.actionTake_survey_to_improve_the_project = QAction(main_window)
        self.actionTake_survey_to_improve_the_project.setObjectName(u"actionTake_survey_to_improve_the_project")
        self.actionTake_survey_to_improve_the_project.setFont(font)
        self.actionCurrent_Version = QAction(main_window)
        self.actionCurrent_Version.setObjectName(u"actionCurrent_Version")
        self.actionCurrent_Version.setFont(font)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"aqua")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBoxWellSelect = QComboBox(self.centralwidget)
        self.comboBoxWellSelect.setObjectName(u"comboBoxWellSelect")
        self.comboBoxWellSelect.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(12)
        self.comboBoxWellSelect.setFont(font1)
        self.comboBoxWellSelect.setMaxVisibleItems(25)

        self.gridLayout_2.addWidget(self.comboBoxWellSelect, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(1200, 800))
        self.tabWidget.setFont(font1)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setMovable(False)
        self.tabMainMenu = QWidget()
        self.tabMainMenu.setObjectName(u"tabMainMenu")
        self.label = QLabel(self.tabMainMenu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 20, 201, 61))
        font2 = QFont()
        font2.setFamily(u"Cascadia Mono")
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.wellListView = QListView(self.tabMainMenu)
        self.wellListView.setObjectName(u"wellListView")
        self.wellListView.setGeometry(QRect(10, 40, 341, 511))
        self.wellListView.setFont(font1)
        self.wellListView.setFrameShadow(QFrame.Sunken)
        self.wellListLabel = QLabel(self.tabMainMenu)
        self.wellListLabel.setObjectName(u"wellListLabel")
        self.wellListLabel.setGeometry(QRect(30, 10, 141, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code SemiBold")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.wellListLabel.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u"resources/4288576 - and application internet seo technology web website.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabMainMenu, icon2, "")
        self.tabProductionPlots = QWidget()
        self.tabProductionPlots.setObjectName(u"tabProductionPlots")
        self.gridLayout = QGridLayout(self.tabProductionPlots)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tabProductionPlots)
        self.groupBox.setObjectName(u"groupBox")
        font4 = QFont()
        font4.setFamily(u"Cascadia Code SemiBold")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.groupBox.setFont(font4)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBoxPhase = QComboBox(self.groupBox)
        self.comboBoxPhase.setObjectName(u"comboBoxPhase")
        self.comboBoxPhase.setFont(font1)

        self.verticalLayout.addWidget(self.comboBoxPhase)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.verticalLayout.addWidget(self.label_3)

        self.comboBoxUnits = QComboBox(self.groupBox)
        self.comboBoxUnits.setObjectName(u"comboBoxUnits")
        self.comboBoxUnits.setFont(font1)

        self.verticalLayout.addWidget(self.comboBoxUnits)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.verticalLayout.addWidget(self.label_4)

        self.dateEditCurveStart = QDateEdit(self.groupBox)
        self.dateEditCurveStart.setObjectName(u"dateEditCurveStart")
        self.dateEditCurveStart.setFont(font1)
        self.dateEditCurveStart.setCalendarPopup(True)
        self.dateEditCurveStart.setDate(QDate(2020, 1, 1))

        self.verticalLayout.addWidget(self.dateEditCurveStart)

        self.horizontalSliderDate = QSlider(self.groupBox)
        self.horizontalSliderDate.setObjectName(u"horizontalSliderDate")
        self.horizontalSliderDate.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSliderDate)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout.addWidget(self.label_5)

        self.spinBoxRate = QSpinBox(self.groupBox)
        self.spinBoxRate.setObjectName(u"spinBoxRate")
        self.spinBoxRate.setFont(font1)
        self.spinBoxRate.setMaximum(1000000)
        self.spinBoxRate.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.verticalLayout.addWidget(self.spinBoxRate)

        self.horizontalSliderRate = QSlider(self.groupBox)
        self.horizontalSliderRate.setObjectName(u"horizontalSliderRate")
        self.horizontalSliderRate.setMaximum(1000000)
        self.horizontalSliderRate.setSingleStep(100)
        self.horizontalSliderRate.setSliderPosition(0)
        self.horizontalSliderRate.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSliderRate)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.verticalLayout.addWidget(self.label_6)

        self.doubleSpinBoxDi = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxDi.setObjectName(u"doubleSpinBoxDi")
        self.doubleSpinBoxDi.setFont(font1)
        self.doubleSpinBoxDi.setSingleStep(0.500000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBoxDi)

        self.horizontalSliderDi = QSlider(self.groupBox)
        self.horizontalSliderDi.setObjectName(u"horizontalSliderDi")
        self.horizontalSliderDi.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSliderDi)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.verticalLayout.addWidget(self.label_7)

        self.doubleSpinBoxBFactor = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxBFactor.setObjectName(u"doubleSpinBoxBFactor")
        self.doubleSpinBoxBFactor.setFont(font1)
        self.doubleSpinBoxBFactor.setMaximum(2.000000000000000)
        self.doubleSpinBoxBFactor.setSingleStep(0.010000000000000)
        self.doubleSpinBoxBFactor.setValue(1.100000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBoxBFactor)

        self.horizontalSliderBFactor = QSlider(self.groupBox)
        self.horizontalSliderBFactor.setObjectName(u"horizontalSliderBFactor")
        self.horizontalSliderBFactor.setMaximum(2)
        self.horizontalSliderBFactor.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSliderBFactor)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.verticalLayout.addWidget(self.label_10)

        self.doubleSpinBoxMinDecline = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxMinDecline.setObjectName(u"doubleSpinBoxMinDecline")
        self.doubleSpinBoxMinDecline.setFont(font1)

        self.verticalLayout.addWidget(self.doubleSpinBoxMinDecline)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.verticalLayout.addWidget(self.label_9)

        self.comboBoxDeclineCurves = QComboBox(self.groupBox)
        self.comboBoxDeclineCurves.setObjectName(u"comboBoxDeclineCurves")
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(10)
        self.comboBoxDeclineCurves.setFont(font5)

        self.verticalLayout.addWidget(self.comboBoxDeclineCurves)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.verticalLayout.addWidget(self.label_8)

        self.lineEditDeclineCurveName = QLineEdit(self.groupBox)
        self.lineEditDeclineCurveName.setObjectName(u"lineEditDeclineCurveName")
        self.lineEditDeclineCurveName.setFont(font1)
        self.lineEditDeclineCurveName.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.lineEditDeclineCurveName)

        self.pushButtonCreateDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonCreateDeclineCurve.setObjectName(u"pushButtonCreateDeclineCurve")
        font6 = QFont()
        font6.setFamily(u"Cascadia Code SemiBold")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButtonCreateDeclineCurve.setFont(font6)
        self.pushButtonCreateDeclineCurve.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButtonCreateDeclineCurve)

        self.pushButtonRemoveDeclineCurves = QPushButton(self.groupBox)
        self.pushButtonRemoveDeclineCurves.setObjectName(u"pushButtonRemoveDeclineCurves")
        self.pushButtonRemoveDeclineCurves.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonRemoveDeclineCurves)

        self.pushButtonPlotDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonPlotDeclineCurve.setObjectName(u"pushButtonPlotDeclineCurve")
        self.pushButtonPlotDeclineCurve.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonPlotDeclineCurve)

        self.pushButtonDeleteDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonDeleteDeclineCurve.setObjectName(u"pushButtonDeleteDeclineCurve")
        self.pushButtonDeleteDeclineCurve.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonDeleteDeclineCurve)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.widgetProductionPlot = QWidget(self.tabProductionPlots)
        self.widgetProductionPlot.setObjectName(u"widgetProductionPlot")
        sizePolicy1.setHeightForWidth(self.widgetProductionPlot.sizePolicy().hasHeightForWidth())
        self.widgetProductionPlot.setSizePolicy(sizePolicy1)
        self.widgetProductionPlot.setSizeIncrement(QSize(10, 10))
        self.widgetProductionPlot.setFont(font1)

        self.gridLayout.addWidget(self.widgetProductionPlot, 0, 1, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u"resources/4288598 - analysis analytics chart data pie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabProductionPlots, icon3, "")
        self.tabCashflowSetup = QWidget()
        self.tabCashflowSetup.setObjectName(u"tabCashflowSetup")
        self.tabCashflowSetup.setFont(font5)
        self.groupBoxCashflowSetup = QGroupBox(self.tabCashflowSetup)
        self.groupBoxCashflowSetup.setObjectName(u"groupBoxCashflowSetup")
        self.groupBoxCashflowSetup.setGeometry(QRect(10, 10, 1081, 481))
        self.groupBoxCashflowSetup.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"resources/4288564 - banking business cash income money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabCashflowSetup, icon4, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1398, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font)
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        main_window.setMenuBar(self.menubar)
        self.toolBar = QToolBar(main_window)
        self.toolBar.setObjectName(u"toolBar")
        main_window.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.actionTutorial)
        self.menu_Help.addAction(self.actionDocumentation)
        self.menu_Help.addAction(self.actionWebsite)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionReport_a_bug)
        self.menu_Help.addAction(self.actionPropose_a_new_feauture)
        self.menu_Help.addAction(self.actionBugs_and_feature_requests)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionContact_project_creator)
        self.menu_Help.addAction(self.actionTake_survey_to_improve_the_project)
        self.menu_About.addAction(self.actionCurrent_Version)
        self.toolBar.addAction(self.actionImport_Data)

        self.retranslateUi(main_window)
        self.actionImport_Data.triggered.connect(main_window.import_data)
        self.horizontalSliderRate.valueChanged.connect(self.spinBoxRate.setValue)
        self.horizontalSliderDate.valueChanged.connect(self.dateEditCurveStart.stepUp)
        self.horizontalSliderDi.valueChanged.connect(self.doubleSpinBoxDi.stepUp)
        self.horizontalSliderBFactor.valueChanged.connect(self.doubleSpinBoxBFactor.stepUp)
        self.comboBoxWellSelect.currentTextChanged.connect(main_window.well_selected)
        self.actionTutorial.triggered.connect(main_window.help_tutorial)
        self.actionDocumentation.triggered.connect(main_window.help_documentation)
        self.actionWebsite.triggered.connect(main_window.help_website)
        self.actionReport_a_bug.triggered.connect(main_window.help_bug)
        self.actionPropose_a_new_feauture.triggered.connect(main_window.help_feature)
        self.actionBugs_and_feature_requests.triggered.connect(main_window.help_open_bugs_features)
        self.actionContact_project_creator.triggered.connect(main_window.help_contact)
        self.actionTake_survey_to_improve_the_project.triggered.connect(main_window.help_take_survey)
        self.actionCurrent_Version.triggered.connect(main_window.about_version)
        self.horizontalSlider.valueChanged.connect(self.doubleSpinBoxMinDecline.stepUp)
        self.spinBoxRate.valueChanged.connect(self.horizontalSliderRate.setValue)
        self.pushButtonCreateDeclineCurve.clicked.connect(main_window.create_decline_curve)
        self.horizontalSliderRate.valueChanged.connect(main_window.create_decline_curve)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PetroAlchemy", None))
        self.actionImport_Data.setText(QCoreApplication.translate("main_window", u"Import Data", None))
#if QT_CONFIG(tooltip)
        self.actionImport_Data.setToolTip(QCoreApplication.translate("main_window", u"Select file containing production data", None))
#endif // QT_CONFIG(tooltip)
        self.actionTutorial.setText(QCoreApplication.translate("main_window", u"Tutorial", None))
        self.actionSponsor.setText(QCoreApplication.translate("main_window", u"Sponsor", None))
        self.actionProject_Website.setText(QCoreApplication.translate("main_window", u"Project Website", None))
        self.actionDocumentation.setText(QCoreApplication.translate("main_window", u"Documentation", None))
        self.actionWebsite.setText(QCoreApplication.translate("main_window", u"Website", None))
        self.actionReport_a_bug.setText(QCoreApplication.translate("main_window", u"Report a bug", None))
        self.actionPropose_a_new_feauture.setText(QCoreApplication.translate("main_window", u"Propose a new feauture", None))
        self.actionBugs_and_feature_requests.setText(QCoreApplication.translate("main_window", u"Bugs and feature requests", None))
        self.actionContact_project_creator.setText(QCoreApplication.translate("main_window", u"Contact project creator", None))
        self.actionTake_survey_to_improve_the_project.setText(QCoreApplication.translate("main_window", u"Take survey to improve the project", None))
        self.actionCurrent_Version.setText(QCoreApplication.translate("main_window", u"Current Version", None))
#if QT_CONFIG(tooltip)
        self.comboBoxWellSelect.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBoxWellSelect.setCurrentText("")
        self.label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Welcome!</span></p></body></html>", None))
        self.wellListLabel.setText(QCoreApplication.translate("main_window", u"Well List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMainMenu), QCoreApplication.translate("main_window", u"Main Menu", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window", u"Decline Curve Analysis", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Select Phase", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Select Units", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Start of Decline Curve", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Initial Rate", None))
        self.label_6.setText(QCoreApplication.translate("main_window", u"Di (effective %), 1/yr", None))
        self.label_7.setText(QCoreApplication.translate("main_window", u"B Factor", None))
        self.label_10.setText(QCoreApplication.translate("main_window", u"Minimum Decline (effective %), 1/yr", None))
        self.label_9.setText(QCoreApplication.translate("main_window", u"Select Existing Decline Curve", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"Enter New Decline Curve Name", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCreateDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Creates decline curve from current parameters and saves it under the name entered in the box</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCreateDeclineCurve.setText(QCoreApplication.translate("main_window", u"Create New Decline Curve", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemoveDeclineCurves.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Removes the decline curves from the plot, but does not delete them form the application</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemoveDeclineCurves.setText(QCoreApplication.translate("main_window", u"Remove Decline Curves", None))
#if QT_CONFIG(tooltip)
        self.pushButtonPlotDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Plots selected decline curve if it already exists</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonPlotDeclineCurve.setText(QCoreApplication.translate("main_window", u"Plot Decline Curve", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDeleteDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Deletes selected decline curve from the application</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDeleteDeclineCurve.setText(QCoreApplication.translate("main_window", u"Delete Decline Curve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProductionPlots), QCoreApplication.translate("main_window", u"Production Plots", None))
        self.groupBoxCashflowSetup.setTitle(QCoreApplication.translate("main_window", u"Cashflow Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCashflowSetup), QCoreApplication.translate("main_window", u"Cashflow Setup", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("main_window", u"&Help", None))
        self.menu_About.setTitle(QCoreApplication.translate("main_window", u"&About", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
    # retranslateUi
