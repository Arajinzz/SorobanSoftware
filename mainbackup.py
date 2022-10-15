import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from mainwindow import Ui_MainWindow
import yuu
import time
import random


class MainW (QtWidgets.QMainWindow):
    def __init__(self):
        super(MainW, self).__init__()

        self.eTime = 0
        self.aTime = 0
        self.howMany = 0
        self.digits = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.start.clicked.connect(self.displayNumbers)

        self.threadclass = ThreadClass(self.howMany, self.digits, self.eTime, self.aTime, self.ui, self.displayNumbers)
        self.threadclass.valsig.connect(self.updateDisplay)

    def updateDisplay(self, val):
        self.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:80pt; color:#55ff00;\">"+val+"</span></p></body></html>")

    def displayNumbers(self):
        self.digits = self.ui.dig.value()
        self.howMany = self.ui.nums.value()
        self.eTime = self.ui.eraseTime.value()
        self.aTime = self.ui.appearTime.value()

        self.threadclass = ThreadClass(self.howMany, self.digits, self.eTime, self.aTime, self.ui, self.displayNumbers)
        self.threadclass.valsig.connect(self.updateDisplay)

        self.ui.start.setEnabled(False)
        self.ui.save.setEnabled(False)

        self.ui.start.clicked.disconnect(self.displayNumbers)

        self.threadclass.start()



class ThreadClass(QtCore.QThread):

    valsig = QtCore.pyqtSignal([str])

    def __init__(self, howMany, digits, eTime, aTime, ui, Func):
        QtCore.QThread.__init__(self)
        self.howMany = howMany
        self.digits = digits
        self.eTime = eTime
        self.aTime = aTime
        self.ui = ui
        self.b = True
        self.Func = Func

    def waitforEnd(self):
        self.b = False

    def run(self):
        
        self.valsig.emit("Start in 3 Seconds")
        time.sleep(1)
        self.valsig.emit("Start in 2 Seconds")
        time.sleep(1)
        self.valsig.emit("Start in 1 Seconds")
        time.sleep(1)
        self.valsig.emit("Start")
        time.sleep(0.4)
        
        X = []
        multiplier = int(9.9999999999 * pow(10, self.digits-1))
        X.append(random.randint(0, multiplier))
        self.valsig.emit(str(X[0]))
        time.sleep(self.aTime/1000)
        print(X[0])
        for _ in range(1, self.howMany):
            self.valsig.emit("")   
            time.sleep(self.eTime/1000)
            x = yuu.getSimpleNumber(yuu.sumList(X), self.digits)
            while x == 0 :
                x = yuu.getSimpleNumber(yuu.sumList(X), self.digits)
            print(x)
            self.valsig.emit(str(x))
            time.sleep(self.aTime/1000)
            X.append(x)
        
        self.valsig.emit("?")
        self.ui.start.setText("Show Result")
        self.ui.start.setEnabled(True)
        self.ui.start.clicked.connect(self.waitforEnd)

        i = 0
        while self.b:
            i = 0
            time.sleep(0.1)

        self.valsig.emit("Result = "+str(yuu.sumList(X)))
        self.ui.start.setEnabled(False)
        self.ui.start.setText("Start")
        self.ui.start.clicked.connect(self.Func)
        self.ui.start.setEnabled(True)
        self.ui.save.setEnabled(True)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())