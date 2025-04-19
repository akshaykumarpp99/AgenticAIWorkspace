from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
class Espresso(Coffee):
    def prepare(self):
        return "Espresso Coffee is prepared."
    
class Cuppoccino(Coffee):
    def prepare(self):
        return "Cuppoccino Coffee is prepared."
    
class Latte(Coffee):
    def prepare(self):
        return "Latte Coffee is prepared."

class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Cuppoccino":
            return Cuppoccino().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        else:
            return "Coffee not defined"

if __name__ == "__main__":
    coffee = CoffeeMachine()
    print(coffee.make_coffee("Latte"))