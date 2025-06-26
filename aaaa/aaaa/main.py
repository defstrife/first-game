class Product:
    def __init__(self, price, weight, amount, title):
        self.price = price
        self.weight = weight
        self.amount = amount
        self.title = title

    def payment(self):
        a = (100 - self.amount)/100
        b = a*self.price
        return b


bread = Product(100, 0.4, 10, "хлеб")

print(bread.payment())