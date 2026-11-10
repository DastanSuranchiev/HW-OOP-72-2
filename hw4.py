rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def convert_to_kgs(self):
        if self.currency in rates:
            return self.amount * rates[self.currency]
        else:
            return("такую валюту не принимаем")


    def __add__(self, other):
        if self.currency != other.currency:
            return self.convert_to_kgs() + other.convert_to_kgs()
        else:
            return self.amount + other.amount


    def __sub__(self, other):
        if self.currency != other.currency:
            return self.convert_to_kgs() - other.convert_to_kgs()
        else:
            return self.amount - other.amount

    def __mul__(self, other):
        if self.currency != other.currency:
            return self.convert_to_kgs() * other.convert_to_kgs()
        else:
            return self.amount * other.amount

    def __truediv__(self, other):
        if self.currency != other.currency:
            return self.convert_to_kgs() / other.convert_to_kgs()
        else:
            return self.amount / other.amount

    def __str__(self):
        return f"{self.amount} {self.currency}"



money1 = Money(100, "USD")
money2 = Money(5000, "KGS")


r = money1 + money2

print(r)

print(money1)