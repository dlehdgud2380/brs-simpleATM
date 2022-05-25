from account import BankUser

class Banking: # Get Account and Enjoy Banking
    def __init__(self, card_serial: str, pin_num: str):
        self.user = BankUser(card_serial=card_serial, card_pin=pin_num)
    def balance(self):
        return self.user.account()
    def deposit(self, money: int, account_index: int):
        self.user.balance_update(account_index, money, 'plus')
    def withdraw(self, money: int, account_index: int):
        self.user.balance_update(account_index, money, 'minus')
    
if __name__ == "__main__":
    asd = Banking(card_serial="23600", pin_num="1234")
    #asd.deposit(10000, 0)
    #print(asd.balance())
    #asd.withdraw(60000, 0)