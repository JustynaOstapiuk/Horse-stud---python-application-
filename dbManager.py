from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData, DateTime
from sqlalchemy_utils import database_exists, create_database
import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# połączenie się z bazą danych za pomocą create_engine
engine = create_engine("mysql+pymysql://root:@localhost/newdb2")
metadata = MetaData(engine)
# opisywanie tabel z diagramu UML, opisywanie kolumn, ich pól i typów, tworzenie relacji między obiektami, kluczy głównych i obcych
Table('function', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('name', String(32), nullable=False))

Table('user', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('func_id', Integer, ForeignKey('function.id'), nullable=False),
      Column('surname', String(64), nullable=True),
      Column('name', String(64), nullable=True),
      Column('address', String(128), nullable=True),
      Column('phone', String(16), nullable=True))

Table('owner', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=False))

Table('horse', metadata,
      Column('horse_id', Integer, primary_key=True, autoincrement=True),
      Column('name', String(32), nullable=True),
      Column('father_id', Integer, ForeignKey('horse.horse_id'), autoincrement=True),
      Column('mother_id', Integer, ForeignKey('horse.horse_id'), autoincrement=True),
      Column('race', String(30), nullable=True),
      Column('birth', String(30), nullable=True),
      Column('sex', String(20), nullable=True),
      Column('owner_id', Integer, ForeignKey('owner.id'), nullable=True))

Table('stable', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('address', String(128), nullable=True))

Table('stable/horse', metadata,
      Column('stable_id', Integer, ForeignKey('stable.id'), nullable=True),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True))

Table('schedule', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('date', DateTime),
      Column('fodder', String(128), nullable=True),
      Column('supplementation', String(128), nullable=True),
      Column('complementary_foods', String(128), nullable=True))

Table('feeding', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('schedule_id', Integer, ForeignKey('schedule.id'), nullable=True),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=True),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True),
      Column('date', DateTime))

Table('visit', metadata,
      Column('id', Integer, primary_key=True, nullable=False),
      Column('horse_id', Integer, ForeignKey('horse.id'), nullable=True),
      Column('user_id', Integer, ForeignKey('user.id'), nullable=True),
      Column('date', DateTime),
      Column('purpose', String(128), nullable=True))

metadata.create_all((engine))
print(database_exists(engine.url))


