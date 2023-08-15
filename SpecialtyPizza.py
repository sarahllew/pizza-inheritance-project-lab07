
from Pizza import *

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        if size == "S":
            self.price = 12.00
        elif size == "M":
            self.price = 14.00
        else:
            self.price = 16.00
        self.name = name

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.size, self.name, self.price)


sp1 = SpecialtyPizza("S", "Carne-more")

assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
