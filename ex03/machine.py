import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self) -> None:
        self.brokenCount = 10

    def repair(self) -> None:
        self.brokenCount = 10

    def serve(self, drink: type) -> HotBeverage:
        if self.brokenCount <= 0:
            raise CoffeeMachine.BrokenMachineException
        self.brokenCount -= 1
        #50% chance of returning an empty cup
        if random.randint(0, 1) == 1:  
            return CoffeeMachine.EmptyCup()
        return drink()

def test():
    coffeeMachine = CoffeeMachine()
    for _ in range(24):
        try:
            print(coffeeMachine.serve(random.choice(
                [Coffee, Tea, Cappuccino, Chocolate, HotBeverage])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()

if __name__ == '__main__':
    test()
