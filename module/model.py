# Database modeling and Create

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import sqlite3

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    password = Column(String(30))
    card_serial = Column(String(5), nullable=True)
    accounts = relationship("Account", backref="User")

class Account(Base):
    __tablename__ = "account"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(30), ForeignKey("user.name"))
    owner = Column(String(50))
    serial = Column(String(5))
    balance = Column(Integer)
    
class Card(Base):
    __tablename__ = "card"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    owner = Column(String(30))
    serial = Column(String(5))
    pin = Column(String(4))

    
def create_db():
    conn = sqlite3.connect("../database/account.db")
    conn.close()
    engine = create_engine("sqlite:///../database/account.db", echo=True, future=True)
    Base.metadata.create_all(engine)
    
if __name__ == '__main__':
    create_db()