# Account Search Module and Banking

from model import User, Account, Card
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./account.db", echo=True, future=True)

class Banking: # Get Account and Enjoy Banking
    def __init__(self, pin_num: str):
        pass
    def search(self):
        pass
    def add_account(self):
        pass
    def balance(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
    
class Register: # Register to Banking System
    def __init__(self, name):
        with Session(engine) as session:
            new_user = User(
                name=name,
                accounts=[
                    Account(serial='21234', pin='1234')
                ],
            )
        session.add_all([new_user])
        session.commit()
    def account_add(self):
        pass
    def card_add(self):
        pass

class Unregister: # Unregister from Banking System
    pass

if __name__ == '__main__':
    Register("hello")