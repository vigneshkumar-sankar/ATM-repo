#imports
import json
import os




#-------------------------Account--------------------------
class Account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def get_pin(self):
        return self.pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance for {self.name}: {self.balance}")

    def get_balance(self):
        return self.balance
    
#-------------------------ATM--------------------------
class ATM:
    FILE = "accounts.json"

    def __init__(self):
        self.accounts = self.load_accounts()
        self.current_account = None

    def load_accounts(self):
        if not os.path.exists(self.FILE):
            return {}
        
        with open(self.FILE, 'r') as f:
            return json.load(f)
        
    def save_accounts(self):
        with open(self.FILE, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def create_account(self):
        pin = input("Create PIN(4-D): ")

        if pin in self.accounts:
            print("This PIN already exists.")
            return
        balance = int(input("Initial Balance: "))
        self.accounts[pin] = balance
        self.save_accounts()
        print("Account created successfully.")

    def login(self):
        pin = input("Enter PIN: ")
        if pin not in self.accounts:
            print("Invalid PIN.")
        else:
            self.current_account = Account(pin, self.accounts[pin])
            
            if pin not in self.accounts:
                print("Invalid PIN.")
                return False
            
            self.current_account = Account(pin, self.accounts[pin])
            print(f"Login Successful, {pin}!")
            return True
        
    def menu(self):
       if not self.current_account:
            print("Please login first.")
            return
       
       while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.current_account.check_balance()
            elif choice == '2':
                amount = int(input("Enter amount to deposit: "))
                self.current_account.deposit(amount)
                self.save_accounts()
            elif choice == '3':
                amount = int(input("Enter amount to withdraw: "))
                self.current_account.withdraw(amount)
                self.save_accounts()
            elif choice == '4':
                self.accounts[self.current_account.get_pin()] = self.current_account.get_balance()
                self.save_accounts()
                print("Logging out...")
                self.current_account = None
                break 
           
#-------------------------main--------------------------

my_atm = ATM()

while True:
    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        my_atm.create_account()
    elif choice == '2':
        if my_atm.login():
            my_atm.menu()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid option..")

#---- End of Code ---






