# Account Search Module and Banking

from model import User, Account, Card
from sqlalchemy.orm import Session
from random import randint
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./account.db", echo=False, future=True)
    
class Register: # Register to Banking System
    def __init__(self, name, password, owner):
        self.name = name
        self.owner = owner
        self.password = password
        self.account_serial = None
        
        with Session(engine) as session:
            find_user = session.query(User).filter(User.name == self.name, User.password == self.password).first()
            if bool(find_user) is False: # if user is not found
                new_user = User(
                    name=self.name,
                    password=self.password,
                    account=[
                        Account(
                            owner = self.owner, 
                            serial=f'1{str(randint(1000, 9999))}', # serial generation 11000~19999
                            balance=0,
                            card_serial='None'
                        )
                    ],
                )
                session.add(new_user)
                session.commit()
                print('account created')
            else: # User already exists
                print('already exists')
                get_account = session.query(Account).filter(Account.username == self.name, Account.owner == self.owner).first()
                self.account_serial = get_account.serial
                
    def account_add(self):
        
                
    def card_add(self, pin: str):
        card_serial = f'2{str(randint(1000, 9999))}' # serial generation 21000~29999
        with Session(engine) as session:
            new_card = Card(
                owner=self.owner,
                serial=card_serial,
                pin=pin,
            )
            
            # update account info
            account = session.query(Account).filter(Account.serial == self.account_serial).first()
            # print(account.owner)
            account.card_serial = card_serial
            
            session.add(new_card)
            session.commit()

class Unregister: # Unregister from Banking System
    pass


class UserInfo:
    pass
    def userinfo():
        pass
    def account():
        pass
    def card():
        pass
    

if __name__ == '__main__':
    Register("hello", "hello123", "watson").card_add('1234')
    #Register.card_add('18339', '1234')