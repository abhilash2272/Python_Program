class BankAccount:
    __balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Successfully {amount} withdrawn")
        else:
            print("Insufficient balance :")
    def getbalance(self):
        return self.__balance
class SavingAccount(BankAccount):
    def show_balance(self):
        print(f"Balance from SavingAccount: {self.getbalance()}")
b = SavingAccount()
b.deposit(5000)
b.show_balance()
b.withdraw(2000)
b.show_balance()
