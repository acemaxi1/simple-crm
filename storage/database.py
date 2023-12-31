"""
sqlalcamy
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
sqlite relation database
"""
DATABASE_URL = "sqlite:///./storage/orders.db"


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
