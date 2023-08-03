import random

print("\n******WELCOME TO UBA BANK******")
print("____________________________________________\n")
print("--------ACCOUNT CREATION--------")
name = input("\nEnter your full name: ")
account_number = random.randint(1000000000, 10000000000)
print("Your account number is: " + str(account_number))
while True:
    pin = input("Enter your four digit pin: ")
    if len(pin) == 4 and pin.isdigit():
        print("Done...")
        break
    else:
        print("Pin must not be more than four digit. Please try again.")
print("Your Account has been successfully created......\n")


class Atm:

    def __init__(self):
        self.balance = 1000
        self.name = name
        self.account_number = account_number
        self.pin = pin

    def transaction_menu(self):
        print("""
             TRANSACTION MENU
        ****************************
        Menu:
        1: Account Detail
        2: Check Balance
        3: Withdrawal
        4: Deposit
        5: Transfer
        6: Exit
        """)

        while True:
            try:
                option = int(input("Enter 1,2,3,4,5 or 6: "))
            except:
                print("Error: Enter 1,2,3,4,5 or 6 only!\n")
                continue
            else:
                if option == 1:
                    Atm.account_detail()
                elif option == 2:
                    Atm.check_balance()
                elif option == 3:
                    Atm.withdraw(amount=self)
                elif option == 4:
                    Atm.deposit(amount=self)
                elif option == 5:
                    Atm.transfer(amount=self)
                elif option == 6:
                    print("""
                    -----------------------------------------
                    | Thank You for choosing us as your bank |
                    | Do visit us again. Thank you.          |
                    -----------------------------------------
                    """)
                    exit()

    def account_detail(self):
        print(f"\n__________ACCOUNT DETAIL__________")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"PIN: {self.pin}")
        print(f"Available Balance: ${self.balance}\n")

    def check_balance(self):
        balance = self.balance
        print(f'Your current balance is: ${self.balance}\n')

    def withdraw(self, amount):
        amount = int(input("How much do you want to withdraw: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Withdrawal successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print(f'insufficient funds')

    def deposit(self, amount):
        amount = int(input("How much do you want to Deposit: $"))
        self.balance += amount
        while True:
            pin = input("Enter your 4 digit pin to proceed: ")
            if pin == self.pin:
                print("Verified...")
                break
            else:
                print("Wrong pin. Please Check your pin and try again.")
        print("Deposit successful.....")
        print(f'Your current balance is ${self.balance}\n')

    def transfer(self, amount):
        print("""
               SELECT BANK
           ********************
           MENU:
           1: FIRST BANK
           2: GTB BANK
           3: WEMA BANK
           4: STANBIC BANK
           5: ZENITH BANK
           6: KUDA
           7: OPAY
           8: PALMPAY
           9: KEYSTONE BANK
           10: POLARIS BANK
           11: CASHAPP
           12: PAYPAL
           13: ZELLE
           14: BITCOIN
           15: VENMO
           """)
        while True:
            try:
                choice = int(input("Enter 1,2,3,4,5,6,7,8,9,10,11,12,13,14 or 15: "))
            except:
                print("Error: Enter 1,2,3,4,5,6,7,8,9,10,11,12,13,14 or 15 only:  ")
                continue
            else:
                if choice == 1:
                    Atm.first_bank()
                    return Atm.transaction_menu()
                elif choice == 2:
                    Atm.gtb()
                    return Atm.transaction_menu()
                elif choice == 3:
                    Atm.wema()
                    return Atm.transaction_menu()
                elif choice == 4:
                    Atm.stanbic()
                    return Atm.transaction_menu()
                elif choice == 5:
                    Atm.zenith()
                    return Atm.transaction_menu()
                elif choice == 6:
                    Atm.kuda()
                    return Atm.transaction_menu()
                elif choice == 7:
                    Atm.opay()
                    return Atm.transaction_menu()
                elif choice == 8:
                    Atm.palmpay()
                    return Atm.transaction_menu()
                elif choice == 9:
                    Atm.keystone()
                    return Atm.transaction_menu()
                elif choice == 10:
                    Atm.polaris()
                    return Atm.transaction_menu()
                elif choice == 11:
                    Atm.cashapp()
                    return Atm.transaction_menu()
                elif choice == 12:
                    Atm.paypal()
                    return Atm.transaction_menu()
                elif choice == 13:
                    Atm.zelle()
                    return Atm.transaction_menu()
                elif choice == 14:
                    Atm.bitcoin()
                    return Atm.transaction_menu()
                elif choice == 15:
                    Atm.venmo()
                    return Atm.transaction_menu()

    def first_bank(self):
        print("...FIRST BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def gtb(self):
        print("...GTB BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def wema(self):
        print("...WEMA BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def stanbic(self):
        print("...STANBIC BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def zenith(self):
        print("...ZENITH BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def kuda(self):
        print("...KUDA BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def opay(self):
        print("...OPAY BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def palmpay(self):
        print("...PALMPAY BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def keystone(self):
        print("...KEYSTONE BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def polaris(self):
        print("...POLARIS BANK...")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def cashapp(self):
        print("....CASHAPP....")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def paypal(self):
        print("....PAYPAL....")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def zelle(self):
        print("....ZELLE....")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def bitcoin(self):
        print("....BITCOIN....")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")

    def venmo(self):
        print("....VENMO....")
        while True:
            account = input("Enter Account Number: ")
            if len(account) == 10 and account.isdigit():
                print("okay...")
                break
            else:
                print("Account number should not be more than 10 digits. Please check and try again...")
        amount = int(input("Enter transfer amount: $"))
        if self.balance >= amount:
            self.balance -= amount
            while True:
                pin = (input("Enter your 4 digit pin to proceed: "))
                if pin == self.pin:
                    print("Verified...")
                    break
                else:
                    print("Wrong pin. Please Check your pin and try again.")
            print(f'Transfer Successful......')
            print(f'Your current balance is ${self.balance}\n')
        else:
            print("Insufficient Funds")


Atm = Atm()

while True:
    transaction = input("Do you want to perform any transaction?(y/n): ")
    if transaction == "y":
        Atm.transaction_menu()
    elif transaction == "n":
        print("""
            -----------------------------------------
            | Thank You for choosing us as your bank |
            | Do visit us again. Thank you.          |
            -----------------------------------------
            """)
        break
    else:
        print("Wrong command! Enter 'y' for yes and 'n' for no.\n")
