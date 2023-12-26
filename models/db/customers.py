from sqlalchemy import Column, Integer, String
from storage.database import Base, Session
from models.db.base import BaseCRUDModel
from sqlalchemy.sql.expression import select


class Customer(Base, BaseCRUDModel):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String)
    customer_name = Column(String)

    @classmethod
    def get_names(cls):
        with Session() as db:
            stmt = select(cls.customer_name)
            return db.execute(stmt).all()
