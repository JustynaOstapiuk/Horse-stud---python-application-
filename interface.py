import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
# stworzenie głównego okna
def say_hello():
    print("Hi")

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Baza danych stajni")
        self.setGeometry(500,500,500,500)
        self.setButton()
# dodanie przycisków
    def setButton(self):
        button1 = QPushButton("Stajnie")
        button1.move(200, 300)


        button1.clicked.connect(say_hello)

        button1.show()
        button2 = QPushButton("Konie")
        button2.move(200, 300)
        button3 = QPushButton("Daty wpisu koni do stajni")
        button3.move(200, 300)
        button4 = QPushButton("Funkcje użytkownika")
        button4.move(200, 300)
        button5 = QPushButton("Użytkownicy")
        button5.move(200, 300)
        button6 = QPushButton("Właściciele")
        button6.move(200, 300)
        button7 = QPushButton("Wizyty")
        button7.move(200, 300)
        button8 = QPushButton("Harmonogramy")
        button8.move(200, 300)
        button9 = QPushButton("Karmienie")
        button9.move(200, 300)
        button10 = QPushButton("Dodaj stajnię")
        button10.move(200,300)
        button11 = QPushButton("Dodaj konia")
        button11.move(200, 300)
        button12 = QPushButton("Dodaj datę wpisu konia do stajni")
        button12.move(200, 300)
        button13 = QPushButton("Dodaj funkcję użytkownika")
        button13.move(200, 300)
        button14 = QPushButton("Dodaj użytkownika")
        button14.move(200, 300)
        button15 = QPushButton("Dodaj właściciela")
        button15.move(200, 300)
        button16 = QPushButton("Dodaj wizytę")
        button16.move(200,300)
        button17 = QPushButton("Dodaj harmonogram")
        button17.move(200, 300)
        button18 = QPushButton("Dodaj karmienie")
        button18.move(200, 300)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button8)
        layout.addWidget(button9)
        layout.addWidget(button10)
        layout.addWidget(button11)
        layout.addWidget(button12)
        layout.addWidget(button13)
        layout.addWidget(button14)
        layout.addWidget(button15)
        layout.addWidget(button16)
        layout.addWidget(button17)
        layout.addWidget(button18)

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
