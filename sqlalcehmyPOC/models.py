from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date


class SQLAlchemyTable(Base):
    __tablename__ = 'sqlalchemy_table'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String, index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)


class Sales(Base):
    __tablename__ = 'sales_record'

    region = Column(String),
    country = Column(String),
    item_type = Column(String),
    sales_channel = Column(String),
    order_priority = Column(String),
    order_date = Column(String),
    order_id = Column(String, primary_key=True),
    ship_date = Column(String),
    units_sold = Column(String),
    unit_price = Column(String),
    unit_cost = Column(String),
    total_revenue = Column(String),
    total_cost = Column(String),
    total_profit = Column(String)