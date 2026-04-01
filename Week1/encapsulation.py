# Class example using the property decorator.
class BankAccount:
    bank_name = "Harsh Global Bank"         # Class variable

    def __init__(self, account_number, name, amount):
        # when the variables are represented with the self parameter they become instance variables.
        self._account_number = account_number   # Protected naming standard in python. Will be still accessible but not encouraged.
        self.name = name                        # public variable accessible everywhere using the object instance.        
        self.__balance = amount                 # Private variable uses name mangling in order to prevent unnecessary overrides but still accessible.

    # @property asks python to treat the python it's decorating as a standard attribute
    @property
    def balance(self):
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


class BankAcc:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def set_balance(self, amount):
        self.__balance += amount if amount > 0 else 0
        return f"Deposited {amount}"

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":

    # object creation with class object where getters and setters are created using @property.
    my_account = BankAccount(5575, "Prakash", 1000)
    print(my_account.balance)       

    # calling the deposit function
    my_account.deposit(2000)
    print("After deposit: ", my_account.balance)

    # calling the withdrawal function
    my_account.withdraw(1000)
    print("After Withdrawal: ", my_account.balance)

    # Using name mangling to return the variable with private naming standard.
    print(my_account._BankAccount__balance)



    # object creation of a class without @property decorator creating the getters and setters.
    account = BankAcc("Aditi", 100000)
    # use name mangling standard to view the variable.
    print("Initial Balance: ", account._BankAcc__balance)

    print("Using setter for balance updation: ", account.set_balance(1000))
    print("Balance after deposit using getter for balance: ", account.get_balance())

    # doesn't allow you to access the variable directly
    # print(account.__balance)

    # use name mangling standard to view the variable.
    print("Using name mangling for retrieving the balance value", account._BankAcc__balance)
