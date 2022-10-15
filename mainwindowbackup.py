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
        MainWindow.resize(910, 678)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 72pt \"Arial\";\n"
"background-color: rgb(74, 74, 74);")
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setStyleSheet("QGroupBox {\n"
"  border: 1px solid black;\n"
"  border-radius: 5px;\n"
"}")
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupbox)

        self.verticalLayout_4.setContentsMargins(-1, -1, 1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.dig = QtWidgets.QSpinBox(self.groupbox)
        self.dig.setMinimum(2)
        self.dig.setMaximum(9)
        self.dig.setObjectName("dig")
        self.horizontalLayout_2.addWidget(self.dig)

        self.label_4 = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.nums = QtWidgets.QSpinBox(self.groupbox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nums.setFont(font)
        self.nums.setMinimum(2)
        self.nums.setMaximum(1000000)
        self.nums.setObjectName("nums")

        self.horizontalLayout_5.addWidget(self.nums)
        self.label_5 = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.groupbox)

        self.groupbox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox1.setAutoFillBackground(False)
        self.groupbox1.setStyleSheet("QGroupBox {\n"
"  border: 1px solid black;\n"
"  border-radius: 5px;\n"
"}")
        self.groupbox1.setFlat(False)
        self.groupbox1.setObjectName("groupbox1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addSub = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.addSub.setFont(font)
        self.addSub.setChecked(True)
        self.addSub.setObjectName("addSub")
        self.verticalLayout_3.addWidget(self.addSub)

        self.horizontalLayout.addWidget(self.groupbox1)
        self.groupbox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox2.setStyleSheet("QGroupBox {\n"
"  border: 1px solid black;\n"
"  border-radius: 5px;\n"
"}")
        self.groupbox2.setObjectName("groupbox2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupbox2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.simple = QtWidgets.QRadioButton(self.groupbox2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.simple.setFont(font)
        self.simple.setChecked(True)
        self.simple.setObjectName("simple")
        self.verticalLayout_5.addWidget(self.simple)
        self.complex5 = QtWidgets.QRadioButton(self.groupbox2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.complex5.setFont(font)
        self.complex5.setObjectName("complex5")
        self.verticalLayout_5.addWidget(self.complex5)
        self.complex10 = QtWidgets.QRadioButton(self.groupbox2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.complex10.setFont(font)
        self.complex10.setObjectName("complex10")
        self.verticalLayout_5.addWidget(self.complex10)
        self.horizontalLayout.addWidget(self.groupbox2)
        self.groupbox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox3.setStyleSheet("QGroupBox {\n"
"  border: 1px solid black;\n"
"  border-radius: 5px;\n"
"}")
        self.groupbox3.setObjectName("groupbox3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupbox3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.appearTime = QtWidgets.QSpinBox(self.groupbox3)
        self.appearTime.setMaximum(10000)
        self.appearTime.setObjectName("appearTime")
        self.horizontalLayout_3.addWidget(self.appearTime)
        self.label_2 = QtWidgets.QLabel(self.groupbox3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.eraseTime = QtWidgets.QSpinBox(self.groupbox3)
        self.eraseTime.setMaximum(10000)
        self.eraseTime.setObjectName("eraseTime")
        self.horizontalLayout_4.addWidget(self.eraseTime)
        self.label_3 = QtWidgets.QLabel(self.groupbox3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.groupbox3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(200, 10, 200, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setIconSize(QtCore.QSize(32, 32))
        self.start.setFlat(False)
        self.start.setObjectName("start")
        self.horizontalLayout_7.addWidget(self.start)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.horizontalLayout_7.addWidget(self.save)


        self.exit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.horizontalLayout_7.addWidget(self.exit)


        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Soroban Trainer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:80pt; color:#55ff00;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "عدد الارقام"))
        self.label_5.setText(_translate("MainWindow", "عدد العمليات"))
        self.addSub.setText(_translate("MainWindow", "جمع و طرح"))
        self.simple.setText(_translate("MainWindow", "بسيط"))
        self.complex5.setText(_translate("MainWindow", "مركب 5"))
        self.complex10.setText(_translate("MainWindow", "مركب 10"))
        self.label_2.setText(_translate("MainWindow", "وقت الظهور\n"
"      (ms)"))
        self.label_3.setText(_translate("MainWindow", "وقت المسح\n"
"      (ms)"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.save.setText(_translate("MainWindow", "Save Excel File"))
        self.exit.setText(_translate("MainWindow", "Exit"))

        

