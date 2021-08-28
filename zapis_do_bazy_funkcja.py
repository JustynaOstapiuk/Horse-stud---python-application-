from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class FunctionModel(Base):
    __tablename__ = 'function'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))


class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textN = QtWidgets.QLabel(text='Nazwa:')

        self.inputN = QtWidgets.QLineEdit()

        layout.addWidget(textN)
        layout.addWidget(self.inputN)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        function = FunctionModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        function.name = self.inputN.text()

        # teraz zapisać do bazy
        sesja.add(function)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
