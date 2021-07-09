from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = 'postgresql://{user}:{password}@{host}:{port}/{db}'.\
    format(user="postgres", password="my_password", host="localhost", port="54320", db="postgres")

engine = create_engine(SQL_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
