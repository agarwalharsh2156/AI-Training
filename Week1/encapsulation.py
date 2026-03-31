class BankAccount:
    bank_name = "Harsh Global Bank"         # Class variable
    def __init__(self, account_number, name, amount):
        # when the variables are represented with the self parameter they become instance variables.
        self._account_number = account_number   # Protected naming standard in python. Will be still accessible but not encouraged.
        self.name = name                        # public variable accessible everywhere using the object instance.        
        self.__balance = amount                 # Private variable uses name mangling in order to prevent unnecessary overrides but still accessible.

    # @property asks python to treat the python it's decorating as a standard attribute
    @property
    def balance(self, amount = 0):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount <= 0:
            return ValueError
        else: self.__balance = amount

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if amount > self.balance : return ValueError
        self.balance = self.balance - amount


my_account = BankAccount(5575, "Prakash", 1000)
print(my_account.balance)       

# calling the deposit function
my_account.deposit(2000)
print("After deposit: ", my_account.balance)

# calling the withdrawal function
my_account.withdraw(1000)
print("After Withdrawal: ", my_account.balance)
