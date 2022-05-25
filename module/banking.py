from account import BankUser

class Banking: # Get Account and Enjoy Banking
    def __init__(self, card_serial: str, pin_num: str):
        self.user = BankUser(card_serial=card_serial, card_pin=pin_num)
    
    def select(self):
        pass
    def balance(self):
        pass
    def deposit(self, doller: int):
        pass
    def withdraw(self, doller: int):
        pass
    
if __name__ == "__main__":
    pass