from Week1.encapsulation import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, amount):
        super().__init__(account_number=account_number, name=name, amount=amount)

    # not a good practice to access a private variable like this.
    # def show(self):
    #     return self._BankAccount__balance

    def show(self):
        return self.balance

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
