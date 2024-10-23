class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficiant Funds")  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Cannot deposit the amount")    
        

    def get_balance(self):
        print(f"{self.__balance}")

ac = BankAccount(50000)  
ac.deposit(10000)    

print(ac._BankAccount__balance)
ac.get_balance()
print(dir(ac))
#  _ protected, __private



