# Account Management Module

from typing import Dict
from model import User, Account, Card
from sqlalchemy.orm import Session
from random import randint
from sqlalchemy import create_engine

import json

engine = create_engine("sqlite:///../database/account.db", echo=False, future=True)
session = Session(engine)
class Register:  # Register to Banking System
    def __init__(self, name: str, password: str, owner: str):
        self.name = name
        self.password = password
        self.owner = owner
    
    def user(self) -> None: # User add to database
    
        user_check = session.query(User).filter(User.name == self.name, User.password == self.password).first()
        if bool(user_check) is False: # register new user
            new_user = User(
                name=self.name,
                password=self.password,
                card_serial=None,
                accounts=[]
            )
            session.add(new_user)
            session.commit()
            print('User registered')
        else: # if account is exists
            print('User already registered')
        
    def card(self, pin) -> None: # card add to database
        card_check = session.query(Card).filter(Card.owner == self.owner, Card.username == self.name).first()
        
        if bool(card_check) is False: # if card is not exists
            card_serial: str = f'2{randint(1000,9999)}'
            new_card = Card(
                username=self.name,
                owner=self.owner,
                serial=card_serial,
                pin=pin
            )
            session.add(new_card)
            user = session.query(User).filter(User.name == self.name, User.password == self.password).first()
            user.card_serial = card_serial
            session.commit()
            print('Card added')
        else: 
            print('Card already exists')
        
    def account(self): # account add to database
        user = session.query(User).filter(User.name == self.name, User.password == self.password).first()
        account_serial: str = f'1{randint(1000,9999)}'
        accounts: list = user.accounts
        
        if len(accounts) >= 3:
            print('Accounts reached maximum')
        else:  
            if bool(user.accounts) is False or account_serial not in accounts:
                new_accounts = Account(
                    username=self.name,
                    owner=self.owner,
                    serial=account_serial,
                    balance=0
                )
                session.add(new_accounts)
                session.commit()
                print('Account added')
            else:
                print('Account already exists')
        
class BankUser: # Search BankUser
    def __init__(self, card_serial: str = "", card_pin: str = "", username: str="", password: str=""):
        
        # for account login variables
        self.username = username
        self.password = password
        self.card_serial = card_serial
        self.card_pin = card_pin
        
        # GET DB Query
        self.user = None
        self.card = None
        
        cardlogin = self.card_login()
        userlogin = self.user_login()
        
        print(f'card_login: {cardlogin}\nuser_login: {userlogin}')
        
        self.info: Dict = {
            "user":{
                "name": self.user.name,
                "card_serial": self.user.card_serial,
            },
            "card":{
                "username": self.card.username,
                "owner": self.card.owner,
                "serial": self.card.serial
            },
            "accounts":{
            }
        }
        
        for index, account in enumerate(self.user.accounts):
            self.info['accounts'][f'{account.serial}'] = {
                'accountId':index,
                'username': account.username,
                'owner': account.owner,
                'serial': account.serial,
                'balance': account.balance
            }
            
    def card_login(self) -> bool:
        if bool(self.card_serial) is True and bool(self.card_pin) is True:
            self.card = session.query(Card).filter(Card.serial == self.card_serial, Card.pin == self.card_pin).first()
            self.user = session.query(User).filter(User.card_serial == self.card.serial).first()
            return True
        else:
            return False
    
    def user_login(self) -> bool:
        if bool(self.username) is True and bool(self.password) is True:
            self.user = session.query(User).filter(User.name == self.username, User.password == self.password).first()
            self.card = session.query(Card).filter(Card.serial == self.user.card_serial, Card.username == self.user.name).first()
            return True
        else:
            return False
        
    def userinfo(self) -> Dict: # user data
        return self.info['user']
    
    def cardinfo(self) -> Dict: # card data
        return self.info['card']
    
    def account(self, serial='') -> Dict: # account data
        if serial == '':
            return self.info['accounts']
        else:
            return self.info['accounts'][f'{serial}']
    
    def balance_update(self, account_index: int, money: int, mode: str) -> None:
        account = self.user.accounts[account_index]
        if mode == 'plus':
            account.balance += money
        elif mode == 'minus':
            test: int = account.balance - money 
            if test < 0:
                print("Can`t Withdraw Money")
            else:
                account.balance -= money
        else:
            print("Incorrect mode")
        session.commit()
            
    def data(self):
        return self.info
    
    def __repr__(self):
        return str(json.dumps(self.info, sort_keys=False, indent=4))

if __name__ == '__main__': # module test
    #asd = Register("hello", "hello123", "watson")
    #asd.user()
    #asd.card("1234")
    #asd.account()
    #print(BankUser(username="hello", password="hello123").data())
    #print(BankUser(card_serial="23600", card_pin="1234").balance_update(0, 10000, 'minus'))
