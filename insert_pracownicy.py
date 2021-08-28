import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class EmployeeModel:
    surname = ''
    name = ''
    address = ''
    phone = ''
    function = ''


class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textS = QtWidgets.QLabel(text='Nazwisko:')
        textN = QtWidgets.QLabel(text='Imię:')
        textA = QtWidgets.QLabel(text='Adres:')
        textP = QtWidgets.QLabel(text='Telefon:')
        textF = QtWidgets.QLabel(text='Funkcja:')

        self.inputS = QtWidgets.QLineEdit()
        self.inputN = QtWidgets.QLineEdit()
        self.inputA = QtWidgets.QLineEdit()
        self.inputP = QtWidgets.QLineEdit()
        self.inputF = QtWidgets.QLineEdit()

        layout.addWidget(textS)
        layout.addWidget(self.inputS)
        layout.addWidget(textN)
        layout.addWidget(self.inputN)
        layout.addWidget(textA)
        layout.addWidget(self.inputA)
        layout.addWidget(textP)
        layout.addWidget(self.inputP)
        layout.addWidget(textF)
        layout.addWidget(self.inputF)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        employee = EmployeeModelModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        employee.surname = self.inputS.text()
        employee.name = self.inputN.text()
        employee.address = self.inputA.text()
        employee.phone = self.inputP.text()
        employee.function = self.inputF.text()

        # zapis do bazy


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
