import pytz
import datetime


class Account:
    """Simple account class with balance"""
    
    @staticmethod   # su _ pradzioj , jis yra non public, only private. 
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []  # Logai
        print("Account created for " + self.name)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))  # kvieciam vidini metoda per klase
    
    def withdraw(self, amount):
        if amount < 0:
            self.balance -= amount
            self.transaction_list.append((self._current_time(), amount)) # galim kviest ir per self, nes privat metodas, static metodas
        else:
            print(f"The amount must be lower than zero")
        self.show_balance()
    
    def show_balance(self):
        print(f"Balance is {self.balance}")    
        
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1  # kad butu minusas
            print(f"{amount} , {transaction_type} on {date}, (local time was : {date.astimezone()})")


if __name__ == '__main__':
    acc_1 = Account("Kasparas",1)
    print(acc_1.name)
    print(acc_1.balance)

    acc_1.deposit(5500)
    acc_1.show_balance()
    acc_1.withdraw(-100)
    acc_1.show_transactions()
    
    print("*"*80)
    
    adele = Account("Adele", 10000)
    adele.deposit(100)
    adele.withdraw(-555)
    adele.show_transactions()
    adele.show_balance()
    print(adele.__dict__)

