from sqlalchemy import create_engine

# print(sqlalchemy.__version__)
"""Establish a connection"""
engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'.
                       format(user="postgres",password="my_password",host="localhost",port="54320",db="postgres"))

"""Declare a mapping"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User (name='%s', fullname='%s', nickname='%s'>".format(self.name, self.fullname, self.nickname)


var = User.__table__
print(var)
"""Create a schema and table"""
Base.metadata.create_all(engine)

"""Create an instance of the mapped class"""
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
print(ed_user.name)
print(str(ed_user.id))

""" Creating a session
The above Session is associated with our SQLite-enabled Engine, but it hasn’t opened any connections yet. 
When it’s first used, it retrieves a connection from a pool of connections maintained by the Engine, and holds onto it 
until we commit all changes and/or close the session object.
"""
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)

pg_session = Session()
""" Adding and Updating Objects"""
pg_session.add(ed_user)

pg_session.commit()

