from email import message
from typing import Dict
from .account import BankUser

class Banking: # Get Account and Enjoy Banking
    def __init__(self, card_serial: str, pin_num: str):
        self.user = BankUser(card_serial=card_serial, card_pin=pin_num)
        self.login: Dict = self.user.card_login()

    def balance(self) -> Dict: # balance check
        if self.login['login'] == True:
            return self.user.account()
        else:
            return self.login
    def deposit(self, money: int, account_index: int) -> Dict:
        if self.login['login'] == True:
            return self.user.balance_update(account_index, money, 'plus')
        else:
            print(self.login)
    def withdraw(self, money: int, account_index: int) -> Dict:
        if self.login['login'] == True:
            return self.user.balance_update(account_index, money, 'minus')
        else:
            print(self.login)
    def login_info(self) -> Dict: # login_info return
        return self.login
            
if __name__ == "__main__":
    #user = Banking(card_serial="21087", pin_num="1234")
    #print(user.login_info())
    #print(user.balance())
    #user.deposit(10000, 0)
    #print(asd.balance())
    #user.withdraw(20000, 0)
    pass 