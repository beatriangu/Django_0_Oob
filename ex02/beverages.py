#!/usr/bin/python3

class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        TEMPLATE = ("name : {name}\n"
                     "price: {price:0.2f}\n"
                     "description: {description}")
        return TEMPLATE.format(name=self.name, price=self.price, description=self.description())


class Coffee(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "coffee"
		self.price = 0.40
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self): 
		super().__init__()
		self.name = "tea"

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "chocolate"
		self.price = 0.50
	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__()
		self.name = "cappuccino"
		self.price = 0.45
	def description(self):
		return "Un po' di Italia nella sua tazza!"

def test():
	print(HotBeverage())
	print(Coffee())
	print(Tea())
	print(Chocolate())
	print(Cappuccino())


if __name__ == '__main__':
	test()