# Database modeling and Create

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import sqlite3

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    accounts = relationship("users", backref="users")

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True)
    owner = Column(String(30), ForeignKey("users.name"))
    serial = Column(String(5))
    cards = relationship("Card", backref="accounts")
    pin = Column(String(4))
    
class Card(Base):
    __tablename__ = "cards"
    
    id = Column(Integer, primary_key=True)
    owner = Column(String(30), ForeignKey("accounts.owner"))
    account = Column(String(30), ForeignKey("accounts.serial"))
    serial = Column(Integer)
    
def create_db():
    conn = sqlite3.connect("account.db")
    conn.close()
    engine = create_engine("sqlite:///./account.db", echo=True, future=True)
    Base.metadata.create_all(engine)
    
if __name__ == '__main__':
    create_db()