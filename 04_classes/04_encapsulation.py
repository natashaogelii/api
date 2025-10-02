# private variables

class Bank:
    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name

    def set_balance(self, balance):
        self.__balance += balance
        #self__balance = self._balance + balance

    def get_balance(self):
        return self.__balance


b = Bank(10, "Te") #create an instance of the class
#print(b.__balance) - you can't access it outside of the function, bc it's private or sth
print(b.name)
print(b.set_balance(5000))
print(b.get_balance())



