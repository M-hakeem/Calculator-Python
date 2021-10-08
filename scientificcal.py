import sys
from PyQt5 import QtWidgets,QtGui,uic

class calculate(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(calculate,self).__init__(parent)
        uic.loadUi("../venv/Lib/site-packages/QtDesigner/scientific.ui", self)
        #uic.loadUi("C:\\Users\\mohammed\\PycharmProjects\\pythonProject\\venv\\Lib\\site-packages\\QtDesigner\\cal.ui",self)
        self.show()

        self.one.clicked.connect(self.method1)
        self.two.clicked.connect(self.method2)
        self.three.clicked.connect(self.method3)
        self.four.clicked.connect(self.method4)
        self.five.clicked.connect(self.method5)
        self.six.clicked.connect(self.method6)
        self.seven.clicked.connect(self.method7)
        self.eight.clicked.connect(self.method8)
        self.nine.clicked.connect(self.method9)
        self.zero.clicked.connect(self.method0)
        self.dot.clicked.connect(self.methoddot)
        self.plus.clicked.connect(self.methodplus)
        self.minus.clicked.connect(self.methodminus)
        self.mult.clicked.connect(self.methodmult)
        self.div.clicked.connect(self.methoddiv)
        self.clear.clicked.connect(self.methodclear)
        self.equals.clicked.connect(self.methodequals)
        self.deleting.clicked.connect(self.methoddel)


    def method1(self):
        text=self.result.text()
        self.result.setText(text+"1")
    def method2(self):
        text=self.result.text()
        self.result.setText(text+"2")
    def method3(self):
        text=self.result.text()
        self.result.setText(text+"3")
    def method4(self):
        text=self.result.text()
        self.result.setText(text+"4")
    def method5(self):
        text=self.result.text()
        self.result.setText(text+"5")
    def method6(self):
        text=self.result.text()
        self.result.setText(text+"6")
    def method7(self):
        text=self.result.text()
        self.result.setText(text+"7")
    def method8(self):
        text=self.result.text()
        self.result.setText(text+"8")
    def method9(self):
        text=self.result.text()
        self.result.setText(text+"9")
    def method0(self):
        text=self.result.text()
        self.result.setText(text+"0")
    def methoddot(self):
        text=self.result.text()
        self.result.setText(text+".")
    def methodplus(self):
        text=self.result.text()
        self.result.setText(text+"+")
    def methodminus(self):
        text=self.result.text()
        self.result.setText(text+"-")
    def methodmult(self):
        text=self.result.text()
        self.result.setText(text+"*")
    def methoddiv(self):
        text=self.result.text()
        self.result.setText(text+"/")
    def methodclear(self):
        self.result.setText("")
    def methoddel(self):
        text=self.result.text()
        self.result.setText(text[:len(text)-1])
    def methodequals(self):
        text=self.result.text()

        try:
            ans=eval(text)
            self.result.setText(str(ans))
        except:
            self.result.setText("wrong input")

app = QtWidgets.QApplication(sys.argv)
window = calculate()
app.setQuitOnLastWindowClosed(True)
app.exec_()