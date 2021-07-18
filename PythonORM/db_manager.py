from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key= True )
    name = Column('name', String)


engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

user = Person()
user.id = 1
user.name = 'Rajesh'

session.add(user)
session.commit()

users = session.query(Person).all()

for usr in users:
    print(usr.id, usr.name)

session.close()