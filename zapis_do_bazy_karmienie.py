from PySide2 import QtWidgets
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScheduleModel(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    feedings = relationship("FeedingModel")

class FeedingModel(Base):
    __tablename__ = 'feeding'
    id = Column(Integer, primary_key=True, autoincrement=True)
    schedule_id = Column(Integer, ForeignKey('schedule.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    horse_id = Column(Integer, ForeignKey('horse.id'))
    date = Column(DateTime)

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    feedings = relationship("FeedingModel")

class HorseModel(Base):
    __tablename__ = 'horse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    feedings = relationship("FeedingModel")

class MyWindow(QtWidgets.QWidget):

    def __init__(self, *args):
        QtWidgets.QWidget.__init__(self, *args)
        self.setGeometry(300, 200, 570, 150)
        layout = QtWidgets.QVBoxLayout(self)
        textS = QtWidgets.QLabel(text='ID harmonogramu:')
        textU = QtWidgets.QLabel(text='ID użytkownika:')
        textH = QtWidgets.QLabel(text='ID konia:')
        textD = QtWidgets.QLabel(text='Data:')

        self.inputS = QtWidgets.QLineEdit()
        self.inputU = QtWidgets.QLineEdit()
        self.inputH = QtWidgets.QLineEdit()
        self.inputD = QtWidgets.QLineEdit()

        layout.addWidget(textS)
        layout.addWidget(self.inputS)
        layout.addWidget(textU)
        layout.addWidget(self.inputU)
        layout.addWidget(textH)
        layout.addWidget(self.inputH)
        layout.addWidget(textD)
        layout.addWidget(self.inputD)

        self.buttonAdd = QtWidgets.QPushButton(text='Dodaj')
        self.buttonAdd.clicked.connect(self.AddToDB)

        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def AddToDB(self):
        feeding = FeedingModel()

        # pobieramy dane dla nowego obiektu z interfejsu:
        feeding.schedule_id = self.inputS.text()
        feeding.user_id = self.inputU.text()
        feeding.horse_id = self.inputH.text()
        feeding.date = self.inputD.text()

        # teraz zapisać do bazy
        sesja.add(feeding)
        sesja.commit()
        sesja.close()


engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
BDSesja = sessionmaker(bind=engine)
sesja = BDSesja()
app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()
