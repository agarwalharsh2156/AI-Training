from Week1.PythonFundamentals.encapsulation import BankAccount, BankAcc

class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, amount):
        super().__init__(account_number=account_number, name=name, amount=amount)

    # not a good practice to access a private variable like this.
    # def show(self):
    #     return self._BankAccount__balance        # python accepts this as balance is a variable from BankAccount class.
    #     return self.__balance                    # python interprets this as _SavingsAccount__balance which doesn't exist. Hence, an error.  

    # method overriding in python for deposit function
    def deposit(self, amount):
        # Adding savings account bonus for each deposit a user makes. Using the setter recieved from @property decorator.
        self.balance += amount + 10
        
    # accessing a private variable from the parent class.
    def show(self):
        return self.balance


# You cannot use the private variable without name mangling format if you don't use @property decorator
# A very important reason to use getters and setters with the help of @property decorator instead of creating your own.
class SavingsAcc(BankAcc):
    def __init__(self, name, balance):
        super().__init__(name = name, balance= balance)

    # the only way to access the balance since balance is a parent class variable which requires name mangling.
    # hence, you should use @property to create setters and use the getters and setters for the variable modification.
    def show(self):
        return self._BankAcc__balance

if __name__ == "__main__":
    # creating an object of the Savings Account.
    sav = SavingsAccount(5575, "Mohit", 100)
    print(f"SavingsAccount-{sav.name}-Balance: ", sav.show())

    # child class accessing methods from parent class.
    # and using the mangled name for accessing the 
    # private attribute from parent class [Not a good practice at all].
    sav.deposit(2000)
    print("After deposit of 2000: ", sav.show())

    # amount available in the bank after withdrawal
    sav.withdraw(200)
    print("Pending amount after withdrawal of 200: ", sav.show())

    #object creation for the class with no @property decorator
    account = SavingsAcc("Aditi", 20000)
    print(account.show())