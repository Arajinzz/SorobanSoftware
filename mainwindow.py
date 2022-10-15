# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 793)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QLabel {\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QLineEdit {\n"
"    background-color:rgb(255,255,255);\n"
"    selection-background-color:rgb(236,116,64);\n"
"    color:rgb(17,17,17);\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color:transparent;\n"
"    color:rgb(17,17,17);\n"
"    selection-background-color:rgb(236,116,64);\n"
"}\n"
"QPushButton{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-bottom-color: rgb(150,150,150);\n"
"    border-right-color: rgb(165,165,165);\n"
"    border-left-color: rgb(165,165,165);\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius:6px;\n"
"    border-top-color: rgb(255,150,60);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 255));\n"
"    border-bottom-color: rgb(200,70,20);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(17,17,17);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-width: 1px;\n"
"    border-top-color: rgba(255,150,60,200);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"    border-bottom-color: rgba(200,70,20,200);\n"
"    border-style: solid;\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    color:rgb(174,167,159);\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(230, 230, 230, 255));\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-style: inset;\n"
"    border-color: rgb(150,150,150);\n"
"    background-color:rgb(221,221,219);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style: solid;\n"
"    border-radius:8px;\n"
"    border-width:1px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(180,180,180);\n"
"    background-color:rgb(247,246,246);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    padding-bottom:2px;\n"
"    padding-top:2px;\n"
"    color:rgb(81,72,65);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(221,218,217,255), stop:1 rgba(240,239,238,255));\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-top-color: rgb(180,180,180);\n"
"    border-left-color: rgb(180,180,180);\n"
"    border-right-color: rgb(180,180,180);\n"
"    border-bottom-color: transparent;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(247,246,246);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QMenuBar {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item {\n"
"    padding-top:4px;\n"
"    padding-left:4px;\n"
"    padding-right:4px;\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QMenuBar::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    padding-top:2px;\n"
"    padding-left:2px;\n"
"    padding-right:2px;\n"
"    border-top-width:2px;\n"
"    border-left-width:2px;\n"
"    border-right-width:2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"    border-style:solid;\n"
"    background-color:rgb(65,64,59);\n"
"    border-top-color: rgb(47,47,44);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"    border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 87, 78, 255), stop:1 rgba(47,47,44, 255));\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(225, 108, 54, 255), stop:1 rgba(246, 134, 86, 255));\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    border-bottom-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(175,85,48,255), stop:1 rgba(236,114,67, 255));\n"
"    border-top-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-right-color:qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"    border-left-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(253,156,113,255), stop:1 rgba(205,90,46, 255));\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(65,64,59);\n"
"}\n"
"QCheckBox {\n"
"    padding:2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(190, 90, 50, 50), stop:1 rgba(250, 130, 40, 50));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"      background-color:rgb(246, 134, 86)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color:rgb(246, 134, 86);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QRadioButton {\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgba(246, 134, 86, 255);\n"
"    color: #a9b7c6;\n"
"    background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(246, 134, 86);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(81,72,65);\n"
"}\n"
"QSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDateTimeEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QDateEdit {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background: #ffffff;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #ffffff;\n"
"    color: rgb(81,72,65);\n"
"    selection-color:rgb(81,72,65);\n"
"    selection-background-color: #ffffff;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color:rgb(81,72,65);    \n"
"    background: #ffffff;\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: rgb(246, 134, 86);\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color:  #1e1d23;    \n"
"    background: #ffffff;\n"
"}\n"
"QFontComboBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color:rgb(81,72,65);\n"
"    background-color: #ffffff;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#f0f0f0;\n"
"}\n"
"QSlider::groove {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"     background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(246, 134, 86);\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"      background: rgb(246, 134, 86);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-color: rgb(255,150,60);\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"      border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"      border-bottom-left-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border: 1px transparent grey;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"     background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"} \n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid;\n"
"    border-color: rgb(207,207,207);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-top-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-bottom-right-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-bottom-left-radius: 7px;\n"
"      border-bottom-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"      border: 1px solid;\n"
"      border-color: rgb(207,207,207);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"      background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"      border: 1px solid;\n"
"      border-color: rgb(255,150,60);\n"
"      border-top-right-radius: 7px;\n"
"      border-top-left-radius: 7px;\n"
"      border-bottom-left-radius: 7px;\n"
"    background: rgb(255, 255, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"      border: 1px solid grey;\n"
"      border-top-left-radius: 7px;\n"
"      border-top-right-radius: 7px;\n"
"      background: rgb(231,231,231);\n"
"     height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(255,150,60);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    border: 1px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"      border: 1px transparent grey;\n"
"      border-bottom-left-radius: 3px;\n"
"      border-bottom-right-radius: 3px;\n"
"      width: 6px;\n"
"      height: 6px;\n"
"      background: rgb(230,230,230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    background-color: transparent;\n"
"     subcontrol-position: top ; /* position at the top left*/ \n"
"     padding:1 1px;\n"
"    \n"
" } \n"
"\n"
"QGroupBox { \n"
"     border: 2px solid gray; \n"
" } ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.mainframe = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mainframe.setFont(font)
        self.mainframe.setAutoFillBackground(False)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainframe)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.mainframe)
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(90)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.horizontalWidget_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QtWidgets.QPushButton(self.mainframe)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setAutoFillBackground(False)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.save = QtWidgets.QPushButton(self.mainframe)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.exit = QtWidgets.QPushButton(self.mainframe)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(1, 1)
        self.tabWidget.addTab(self.mainframe, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalGroupBox = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalGroupBox.setFlat(False)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(70, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.appearTime = QtWidgets.QSpinBox(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.appearTime.setFont(font)
        self.appearTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.appearTime.setMinimum(100)
        self.appearTime.setMaximum(10000)
        self.appearTime.setSingleStep(100)
        self.appearTime.setProperty("value", 400)
        self.appearTime.setObjectName("appearTime")
        self.horizontalLayout_5.addWidget(self.appearTime)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.eraseTime = QtWidgets.QSpinBox(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.eraseTime.setFont(font)
        self.eraseTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eraseTime.setMinimum(100)
        self.eraseTime.setMaximum(10000)
        self.eraseTime.setSingleStep(100)
        self.eraseTime.setProperty("value", 200)
        self.eraseTime.setObjectName("eraseTime")
        self.horizontalLayout_6.addWidget(self.eraseTime)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.verticalGroupBox)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox1.setFont(font)
        self.verticalGroupBox1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.howmany = QtWidgets.QSpinBox(self.verticalGroupBox1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.howmany.setFont(font)
        self.howmany.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.howmany.setWrapping(False)
        self.howmany.setAccelerated(False)
        self.howmany.setMinimum(2)
        self.howmany.setMaximum(10000)
        self.howmany.setProperty("value", 10)
        self.howmany.setObjectName("howmany")
        self.horizontalLayout_7.addWidget(self.howmany)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.digits = QtWidgets.QSpinBox(self.verticalGroupBox1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.digits.setFont(font)
        self.digits.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.digits.setMinimum(2)
        self.digits.setMaximum(7)
        self.digits.setProperty("value", 3)
        self.digits.setObjectName("digits")
        self.horizontalLayout_8.addWidget(self.digits)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.addsub = QtWidgets.QRadioButton(self.verticalGroupBox1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.addsub.setFont(font)
        self.addsub.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addsub.setChecked(True)
        self.addsub.setObjectName("addsub")
        self.verticalLayout_6.addWidget(self.addsub)
        self.verticalLayout_6.setStretch(1, 3)
        self.verticalLayout_6.setStretch(2, 3)
        self.horizontalLayout_3.addWidget(self.verticalGroupBox1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox2.setFont(font)
        self.verticalGroupBox2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.simple = QtWidgets.QCheckBox(self.verticalGroupBox2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.simple.setFont(font)
        self.simple.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.simple.setChecked(True)
        self.simple.setObjectName("simple")
        self.horizontalLayout_11.addWidget(self.simple)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.complex5pos = QtWidgets.QCheckBox(self.verticalGroupBox2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.complex5pos.setFont(font)
        self.complex5pos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.complex5pos.setObjectName("complex5pos")
        self.horizontalLayout_12.addWidget(self.complex5pos)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.complex5neg = QtWidgets.QCheckBox(self.verticalGroupBox2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.complex5neg.setFont(font)
        self.complex5neg.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.complex5neg.setObjectName("complex5neg")
        self.horizontalLayout_13.addWidget(self.complex5neg)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.complex10pos = QtWidgets.QCheckBox(self.verticalGroupBox2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.complex10pos.setFont(font)
        self.complex10pos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.complex10pos.setObjectName("complex10pos")
        self.horizontalLayout_14.addWidget(self.complex10pos)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.complex10neg = QtWidgets.QCheckBox(self.verticalGroupBox2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.complex10neg.setFont(font)
        self.complex10neg.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.complex10neg.setObjectName("complex10neg")
        self.horizontalLayout_15.addWidget(self.complex10neg)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_9.addWidget(self.verticalGroupBox2)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox_2.setFont(font)
        self.verticalGroupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_17.addWidget(self.label_6)
        self.obstacles = QtWidgets.QSpinBox(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.obstacles.setFont(font)
        self.obstacles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.obstacles.setMinimum(1)
        self.obstacles.setMaximum(3)
        self.obstacles.setObjectName("obstacles")
        self.horizontalLayout_17.addWidget(self.obstacles)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.checkBox = QtWidgets.QCheckBox(self.verticalGroupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_16.addWidget(self.checkBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_9.addWidget(self.verticalGroupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_18.addWidget(self.pushButton)
        self.exit2 = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit2.setFont(font)
        self.exit2.setObjectName("exit2")
        self.horizontalLayout_18.addWidget(self.exit2)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Soroban Trainer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">000</span></p></body></html>"))
        self.start.setText(_translate("MainWindow", "ابدأ"))
        self.save.setText(_translate("MainWindow", "حفظ العملية"))
        self.exit.setText(_translate("MainWindow", "الخروج من البرنامج"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainframe), _translate("MainWindow", "الواجهة الرئيسية"))
        self.verticalGroupBox.setTitle(_translate("MainWindow", "اعدادات الوقت"))
        self.label_2.setText(_translate("MainWindow", "وقت ظهور العدد"))
        self.label_3.setText(_translate("MainWindow", "وقت المسح"))
        self.verticalGroupBox1.setTitle(_translate("MainWindow", "اعدادات العمليات"))
        self.label_4.setText(_translate("MainWindow", "طول العملية"))
        self.label_5.setText(_translate("MainWindow", "عدد الارقام في العدد"))
        self.addsub.setText(_translate("MainWindow", "جمع و طرح"))
        self.verticalGroupBox2.setTitle(_translate("MainWindow", "نوع العمليات"))
        self.simple.setText(_translate("MainWindow", "بسيط"))
        self.complex5pos.setText(_translate("MainWindow", "مركب 5 موجب"))
        self.complex5neg.setText(_translate("MainWindow", "مركب 5 سالب"))
        self.complex10pos.setText(_translate("MainWindow", "مركب 10 موجب"))
        self.complex10neg.setText(_translate("MainWindow", "مركب 10 سالب"))
        self.verticalGroupBox_2.setTitle(_translate("MainWindow", "اعدادات الحواجز"))
        self.label_6.setText(_translate("MainWindow", "مستوى الصعوبة"))
        self.checkBox.setText(_translate("MainWindow", "اضافة حواجز "))
        self.pushButton.setText(_translate("MainWindow", "Excel استخراج ملف "))
        self.exit2.setText(_translate("MainWindow", "الخروج من البرنامج"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "الاعدادات"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ASNF SOROBAN من طرف </span></p></body></html>"))

