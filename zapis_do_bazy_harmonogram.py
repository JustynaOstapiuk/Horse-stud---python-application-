from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScheduleModel(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    fodder = Column(String(128))
    supplementation = Column(String(128))
    complementary_foods = Column(String(128))

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textD = QtWidgets.QLabel(text='Data:')
        textF = QtWidgets.QLabel(text='Karmienie:')
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
        schedule = ScheduleModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        schedule.date = self.inputD.text()
        schedule.fodder = self.inputF.text()
        schedule.supplementation = self.inputS.text()
        schedule.complementary_foods = self.inputC.text()

        # teraz zapisać do bazy
        sesja.add(schedule)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
