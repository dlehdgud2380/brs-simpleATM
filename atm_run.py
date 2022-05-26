from module.banking import Banking
import time
import os

cardnum: str = None
cardpin: str = None
user: Banking = None

def process_info(process: str = ''): # Process information
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    print(f"ATM by LeeDongHyeong - {process}")
    print("--------------------------------")

while True: # Process Start
    process_info("Input Card")
    
    while True: # card check
        cardnum = input("Please enter your card number: ")
        cardpin = input("Please enter your card pin: ")
        login = Banking(cardnum, cardpin).login_info()
        if login["login"] == True:
            user = Banking(cardnum, cardpin)
            break
        else:
            process_info("Login Failure")
            print(f'login: {login["login"]}')
            print(login["message"])
            print("\n")
    
    process_info("Login Successful")
    print(f'login: {login["login"]}')
    print(login["message"])
    time.sleep(1)
    
    select_account: int = None
    
    process_info("Select Account")
    while True: # Account Select
        for account in list(user.balance().values()):
            print(f'{account["accountId"]}: {account["serial"]}')
            print(f'balance: ${account["balance"]}')
            print("\n")
        select_account = int(input("select(input number 0~2): "))
        
        if select_account > 2 or select_account < 0:
            process_info("Incorrect Account")
            print("[Please select correct account]")
        else:
            break
        
    process_info("Banking Option")
    while True: # Enjoy Banking
        account = list(user.balance().values())[select_account]
        print(f'Account Serial: {account["serial"]}')
        print(f'Balance: ${account["balance"]}')
        
        option = None
        while True: # option check
            print(f'\n[0: deposit, 1: withdraw]')
            select_option: int = int(input("select option(0~1): "))
            
            if select_option > 1 or select_option < 0:
                process_info("Incorrect Banking Option")
                print("[Please select correct number]")
                print(f'Account Serial: {account["serial"]}')
                print(f'Balance: ${account["balance"]}')
            else:
                option = select_option
                break
        
        money: int = 0
        updated_money: int = 0
        if option == 0: # deposit option
            process_info("Deposit")
            while True: # working check
                print(f'Balance: ${account["balance"]}')
                money = int(input("Please Input Dollar(1~10000): "))
                if money < 1 or money > 10000:
                    print("[Please input correct number]")
                else:
                    break
            user.deposit(money, select_account)
            updated_money = account["balance"] + money
            
        else: # withdraw option
            process_info("Withdraw")
            while True: # working check
                print(f'Balance: ${account["balance"]}')
                money = int(input("Please Input Dollar(1~10000): "))
                if money <= 0 or money > 10000:
                    process_info("Incorrect Number")
                    print("[Please input correct number]")
                elif account["balance"] < money :
                    process_info("Not enough money")
                    print("[Money Not Enough to withdraw]")
                    break
                else:
                    break
            user.withdraw(money, select_account)
            updated_money = 0 if account["balance"]-money < 0 else account["balance"]-money
        break
    
    process_info("Banking Ended")
    print(f'Account Serial: {account["serial"]}')
    print(f'Balance: ${updated_money}')
    
    print("Thank you for Enjoy ATM")
    break