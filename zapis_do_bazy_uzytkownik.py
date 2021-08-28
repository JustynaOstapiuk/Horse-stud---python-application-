from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, ForeignKey, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class FunctionModel(Base):
    __tablename__ = 'function'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    users = relationship("UserModel")

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(50))
    name = Column(String(50))
    address = Column(String(50))
    phone = Column(String(50))
    function_id = Column(Integer, ForeignKey('function.id'))

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 450)
        layout = QtWidgets.QVBoxLayout(self)
        textS = QtWidgets.QLabel(text='Nazwisko:')
        textN = QtWidgets.QLabel(text='Imię:')
        textA = QtWidgets.QLabel(text='Adres:')
        textP = QtWidgets.QLabel(text='Telefon:')
        textF = QtWidgets.QLabel(text='ID funkcji:')

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
        user = UserModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        user.surname = self.inputS.text()
        user.name = self.inputN.text()
        user.address = self.inputA.text()
        user.phone = self.inputP.text()
        user.function_id = self.inputF.text()

        # teraz zapisać do bazy
        sesja.add(user)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
