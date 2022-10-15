import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from mainwindow import Ui_MainWindow
import yuu
import time
import random
import xlwt
import seq
import os.path


class MainW (QtWidgets.QMainWindow):

    def __init__(self):
        super(MainW, self).__init__()

        self.ddk = ''
        self.ssk = seq.keyChecker()

        self.check()

        self.eTime = 0
        self.aTime = 0
        self.howMany = 0
        self.digits = 0
        self.last = []
        self.tchoice = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.save.setEnabled(False)

        self.ui.start.clicked.connect(self.displayNumbers)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.exit2.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.getExcelFile)

        self.threadclass = ThreadClass(self.howMany, self.digits, self.eTime, self.aTime, self.ui, self.displayNumbers, [])
        self.threadclass.valsig.connect(self.updateDisplay)


    def check(self):
        if os.path.isfile('license'):
            f = open("license", "r")
            f = f.readlines()
            f = f[0].replace("\n", "")
            
            self.ddk = f

            if self.ssk != self.ddk:
                text, ok = QtWidgets.QInputDialog.getText(self, 'Enter your key', 'key:')
                if ok:
                    text = str(text).replace("\n", "")
                    self.ddk = text

                    if self.ddk != self.ssk:
                        exit()
                    else:
                        f = open('license', 'w')
                        f.write(self.ddk)
                        f.close()
                else:
                    exit()

        else:
            text, ok = QtWidgets.QInputDialog.getText(self, 'Enter your key', 'key:')
            if ok:
                text = str(text).replace("\n", "")
                self.ddk = text

                if self.ddk != self.ssk:
                    exit()
                else:
                    f = open('license', 'w')
                    f.write(self.ddk)
                    f.close()
            else:
                exit()


    def getNum(self, X):

        self.check()
        
        c = 0

        if len(self.tchoice) == 0 and len(self.last) == 0:
            return yuu.getSimpleNumber(yuu.sumList(X), self.digits)
        else:
            if len(self.tchoice) == 0:
                self.choices = [i for i in self.last]
                self.last = []
            
            c = random.randint(0, len(self.choices)-1)
            c = self.choices.pop(c)
            self.last.append(c)
            

        if c == 1:
            print("COMPLEX 5 POS")
            return yuu.genComplex5(yuu.sumList(X), self.digits)
        elif c == 2:
            print("COMPLEX 5 NEG")
            return yuu.genComplex5Neg(yuu.sumList(X), self.digits)
        elif c == 3:
            print("COMPLEX 10 POS")
            return yuu.genComplex10Pos(yuu.sumList(X), self.digits)
        elif c == 4:
            print("COMPLEX 10 NEG")
            return yuu.genComplex10Neg(yuu.sumList(X), self.digits)


    def getExcelFile(self):

        self.check()

        i, okPressed = QtWidgets.QInputDialog.getInt(self, "أدخل عدد العمليات","عدد العمليات :", 2, 0, 10000, 1)
        if okPressed:

            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","Text Files (*.xls)", options=options)
            if filename:
                self.digits = self.ui.digits.value()
                self.howMany = self.ui.howmany.value()
                self.eTime = self.ui.eraseTime.value()
                self.aTime = self.ui.appearTime.value()

                choices = []
                if self.ui.complex5pos.isChecked():
                    choices.append(1)
                
                if self.ui.complex5neg.isChecked():
                    choices.append(2)

                if self.ui.complex10pos.isChecked():
                    choices.append(3)

                if self.ui.complex10neg.isChecked():
                    choices.append(4)

                self.tchoice = choices

                book = xlwt.Workbook()
                sh1 = book.add_sheet("Sheet 1")
                sh2 = book.add_sheet("Results")


                for col in range(0, i):
                    X = []
                    multiplier = int(9.9999999999 * pow(10, self.digits-1))
                    X.append(random.randint(int(multiplier/10 + 1), multiplier))

                    for _ in range(1, self.howMany):
                        x = self.getNum(X)
                        while x == 0 :
                            x = self.getNum(X)
                        X.append(x)

                    for n, x in enumerate(X):
                        sh1.write(n, col, x)
                    
                    sh2.write(0, col, yuu.sumList(X))

                filename = str(filename).split(".")
                if len(filename) > 1:
                    if filename[len(filename)-1] == ".xls":
                        del filename[len(filename)-1]
                filename = "".join(filename)+".xls"
                book.save(filename)






    def exit(self):
        exit(0)


    def updateDisplay(self, val):
        self.check()
        
        if(val != "" and len(val.split("=")) < 2):
            QtMultimedia.QSound.play("beep.wav")
        self.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:80pt; color:#55ff00;\">"+val+"</span></p></body></html>")

    def displayNumbers(self):

        self.check()

        self.ui.save.setEnabled(False)

        self.digits = self.ui.digits.value()
        self.howMany = self.ui.howmany.value()
        self.eTime = self.ui.eraseTime.value()
        self.aTime = self.ui.appearTime.value()

        choices = []
        if self.ui.complex5pos.isChecked():
            choices.append(1)
        
        if self.ui.complex5neg.isChecked():
            choices.append(2)

        if self.ui.complex10pos.isChecked():
            choices.append(3)

        if self.ui.complex10neg.isChecked():
            choices.append(4)

        self.threadclass = ThreadClass(self.howMany, self.digits, self.eTime, self.aTime, self.ui, self.displayNumbers, choices)
        self.threadclass.valsig.connect(self.updateDisplay)

        self.ui.start.setEnabled(False)

        self.ui.start.clicked.disconnect(self.displayNumbers)

        self.threadclass.start()



class ThreadClass(QtCore.QThread):

    valsig = QtCore.pyqtSignal([str])
    msgboxsig = QtCore.pyqtSignal()

    def __init__(self, howMany, digits, eTime, aTime, ui, Func, choices):
        QtCore.QThread.__init__(self)
        self.howMany = howMany
        self.digits = digits
        self.eTime = eTime
        self.aTime = aTime
        self.ui = ui
        self.b = True
        self.Func = Func
        self.choices = choices
        self.last = []
        self.symbolesEasy = ["A", "B", "C", "D"]
        self.symbolesMedium = [ "b","B", "C", "$", "!", "c","(","+"]
        self.symbolesHard = ["A","a", "(", ")", "!!", "!", "X", "=", "+", "x", "B","b", "-"]
        self.stop = False
        self.gX = []



    def saveE(self):
        
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","Text Files (*.xls)", options=options)
        if filename:
            
            book = xlwt.Workbook()
            sh1 = book.add_sheet("Sheet 1")
            sh2 = book.add_sheet("Results")

            for n, x in enumerate(self.gX):
                sh1.write(n, 0, x)
            
            sh2.write(0, 0, yuu.sumList(self.gX))

            filename = str(filename).split(".")
            if len(filename) > 1:
                if filename[len(filename)-1] == ".xls":
                    del filename[len(filename)-1]
            filename = "".join(filename)+".xls"
            book.save(filename)


    def waitforEnd(self):
        self.b = False


    def Stop(self):
        self.stop = True


    def getNum(self, X):
        
        c = 0

        if len(self.choices) == 0 and len(self.last) == 0:
            return yuu.getSimpleNumber(yuu.sumList(X), self.digits)
        else:
            if len(self.choices) == 0:
                self.choices = [i for i in self.last]
                self.last = []
            
            c = random.randint(0, len(self.choices)-1)
            c = self.choices.pop(c)
            self.last.append(c)
            

        if c == 1:
            print("COMPLEX 5 POS")
            return yuu.genComplex5(yuu.sumList(X), self.digits)
        elif c == 2:
            print("COMPLEX 5 NEG")
            return yuu.genComplex5Neg(yuu.sumList(X), self.digits)
        elif c == 3:
            print("COMPLEX 10 POS")
            return yuu.genComplex10Pos(yuu.sumList(X), self.digits)
        elif c == 4:
            print("COMPLEX 10 NEG")
            return yuu.genComplex10Neg(yuu.sumList(X), self.digits)



    def run(self):
        
        self.valsig.emit("البدء في 3 ثواني")
        time.sleep(1)
        self.valsig.emit("البدء في 2 ثواني")
        time.sleep(1)
        self.valsig.emit("البدء في 1 ثواني")
        time.sleep(1)
        self.valsig.emit("ابدأ")
        time.sleep(0.5)

        obs = []
        chance = 0

        if(self.ui.checkBox.isChecked()):
            dif = self.ui.obstacles.value()
            if(dif == 1):
                obs = self.symbolesEasy
                chance = 2
            elif(dif == 2):
                obs = self.symbolesMedium
                chance = 3
            else:
                obs = self.symbolesHard
                chance = 5
        
        self.ui.start.setEnabled(True)
        self.ui.start.clicked.connect(self.Stop)
        self.ui.start.setText("توقف")
        
        X = []
        multiplier = int(9.9999999999 * pow(10, self.digits-1))
        X.append(random.randint(int(multiplier/10 + 1), multiplier))
        self.valsig.emit(str(X[0]))
        time.sleep(self.aTime/1000)
        print(X[0])
        i = 1
        while(i < self.howMany):

            if(self.stop):
                break
            
            self.valsig.emit("")
            time.sleep(self.eTime/1000)
            if(self.ui.checkBox.isChecked()):
                choice = random.randint(0, chance)
                if(choice != 1 and choice != 0):
                    self.valsig.emit(obs[random.randint(0, len(obs)-1)])
                    time.sleep(self.aTime/1000)
                else:
                    x = self.getNum(X)
                    while x == 0 :
                        x = self.getNum(X)
                    self.valsig.emit(str(x))
                    time.sleep(self.aTime/1000)
                    X.append(x)
                    i+=1

            else:   
                x = self.getNum(X)
                while x == 0 :
                    x = self.getNum(X)
                self.valsig.emit(str(x))
                time.sleep(self.aTime/1000)
                X.append(x)
                i+=1
        
        self.valsig.emit("?")
        self.ui.start.setText("اظهار النتيجة")
        self.ui.start.setEnabled(True)
        self.ui.start.clicked.connect(self.waitforEnd)

        self.gX = X
        self.ui.save.setEnabled(True)
        self.ui.save.clicked.connect(self.saveE)

        while self.b:
            time.sleep(0.1)

        self.valsig.emit(str(yuu.sumList(X))+" = النتيجة")
        self.ui.start.setEnabled(False)
        self.ui.start.setText("ابدا")
        self.ui.start.clicked.connect(self.Func)
        self.ui.start.setEnabled(True)
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainW()
    myapp.show()
    sys.exit(app.exec_())
