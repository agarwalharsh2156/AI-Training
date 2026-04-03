# Bank Account System OOPs design
from datetime import date
class BankAccount:
    bank_name = "PNB Nationals"
    
    
    def __init__(self, holder_name, account_number, initial_deposit):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = initial_deposit
        self.statement = []
        self.statement.append(f"{date.today()} - {self.account_number} - {initial_deposit} - Cr. - {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.statement.append(f"{date.today()} - {self.account_number} - {amount} - Cr. - {self.balance}")
            return f"Deposited {amount}"
        else:
            raise ValueError("Amount should be greater than 0")
        
    
    def withdraw(self, amount):
        if self.balance > amount and amount > 0:
            self.balance -= amount
            self.statement.append(f"{date.today()} - {self.account_number} - {amount} - Dr. - {self.balance}")
            return f"Amount withdrawn: {amount}"
        else:
            return "Insufficient balance."
        
    def monthly_statement(self):
        print("Date --- Account Number --- Amount --- Action --- Balance\n")
        for i in self.statement:
            print(i, "\n")

        

class SavingsAccount(BankAccount):
    interest_rate = 5                   # 5% per annum
    minimum_balance = 1000

    def manage_balance(self):
        # to track the number of days between initial deposit and today. If the difference counts to number of days in an year
        # add the interest amount with respect to balance(based on the banks criterias and policies).
        pass

    def __init__(self, holder_name, account_number, initial_deposit):
        if initial_deposit < self.minimum_balance:
            raise ValueError("Initial Deposit should be more than 1000.")
        else:
            super().__init__(holder_name, account_number, initial_deposit)
            
    def withdraw(self, amount):
        if amount > (self.balance - self.minimum_balance):
            raise ValueError("Minimum balance of 1000 needs to be maintained.")
        else:
            self.balance -= amount
            self.statement.append(f"{date.today()} - {self.account_number} - {amount} - Dr. - {self.balance}")
            return f"Amount withdrawn: {amount}"
        

class CurrentAccount(BankAccount):
    extra_limit = 1000
    interest_rate = 6           # if the customer fails to pay the extra limit withdrawn within 35 days.

    def manage_balance(self):
        # to manage the interest addition on failure of repayment and tracking the days between withdrawal and repayment.
        pass

    def __init__(self, holder_name, account_number, initial_deposit):
        super().__init__(holder_name, account_number, initial_deposit)

    def withdraw(self, amount):
        if amount > (self.balance + self.extra_limit):
            raise ValueError("Minimum balance of 1000 needs to be maintained.")
        else:
            self.balance -= amount
            self.statement.append(f"{date.today()} - {self.account_number} - {amount} - Dr. - {self.balance}")
            return f"Amount withdrawn: {amount}"

            

    





