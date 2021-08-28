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

class OwnerModel(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textO = QtWidgets.QLabel(text='ID właściciela:')
        textU = QtWidgets.QLabel(text='ID użytkownika:')

        self.inputO = QtWidgets.QLineEdit()
        self.inputU = QtWidgets.QLineEdit()

        layout.addWidget(textO)
        layout.addWidget(self.inputO)
        layout.addWidget(textU)
        layout.addWidget(self.inputU)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        owner = OwnerModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        owner.owner_id = self.inputO.text()
        owner.user_id = self.inputU.text()

        # teraz zapisać do bazy
        sesja.add(owner)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
