class BankAccount:
    __balance=0
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if(self.__balance>amount):
            self.__balance-=amount
            print(f"Successsfully {amount} withdrwan")
        else:
            print("Unsufficient balance :")
    def getbalance(self):
        print(f"The current balance in account is {self.__balance}")
b=BankAccount()
b.deposit(5000)
b.getbalance()
b.withdraw(2000)
b.getbalance()
    
