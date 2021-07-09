from sqlalchemy import create_engine

# print(sqlalchemy.__version__)
"""Establish a connection"""
engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'.
                       format(user="postgres",password="my_password",host="localhost",port="54320",db="postgres"))

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users1', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('fullname', String),
 )
metadata.create_all(engine)

ins = users.insert()
print(ins)
ins = users.insert().values(name='jack', fullname='Jack Jones')
conn = engine.connect()
result = conn.execute(ins)