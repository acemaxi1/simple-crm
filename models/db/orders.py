from sqlalchemy import Column, Integer, String, Float, Date
from storage.database import Base
from models.db.base import BaseCRUDModel

class Order(Base, BaseCRUDModel):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    customer_id = Column(String)
    customer_name = Column(String)
    product_id = Column(Integer)
    product_name = Column(String)
    quantity = Column(Integer)
    total_price = Column(Float)
    date = Column(Date)
