import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class ScheduleModel:
    date = ''
    fodder = ''
    supplementation = ''
    complementary_foods = ''

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textD = QtWidgets.QLabel(text='Data:')
        textF = QtWidgets.QLabel(text='Pasza:')
        textS = QtWidgets.QLabel(text='Suplementacja:')
        textC = QtWidgets.QLabel(text='Żywność uzupełniająca:')

        self.inputD = QtWidgets.QLineEdit()
        self.inputF = QtWidgets.QLineEdit()
        self.inputS = QtWidgets.QLineEdit()
        self.inputC = QtWidgets.QLineEdit()

        layout.addWidget(textD)
        layout.addWidget(self.inputD)
        layout.addWidget(textF)
        layout.addWidget(self.inputF)
        layout.addWidget(textS)
        layout.addWidget(self.inputS)
        layout.addWidget(textC)
        layout.addWidget(self.inputC)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        schedule = ScheduleModelModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        schedule.date = self.inputD.text()
        schedule.fodder = self.inputF.text()
        schedule.supplementation = self.inputS.text()
        schedulee.complementary_foods = self.inputC.text()

        # zapis do bazy

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
