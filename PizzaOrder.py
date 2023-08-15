from Pizza import *
from SpecialtyPizza import *
from CustomPizza import *

class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        ''' constructs and returns a str containing time, info for pizza,
            and total order price. calls getPizzaDetails() on objects,
            calls getPrice().'''
        order = ""
        totalprice = 0 
        for i in self.pizzas:
            order += i.getPizzaDetails() + "\n" + "----" + "\n"
        for i in self.pizzas:
            totalprice += i.getPrice()
        return "******\nOrder Time: {}\n{}TOTAL ORDER PRICE: ${:.2f}\n******\n".format(self.time, order, totalprice)


##        
##
##cp1 = CustomPizza("S")
##cp1.addTopping("extra cheese")
##cp1.addTopping("sausage")
##sp1 = SpecialtyPizza("S", "Carne-more")
##order = PizzaOrder(123000) #12:30:00PM
##order.addPizza(cp1)
##order.addPizza(sp1)
##
##
##assert order.getOrderDescription() == \
##"******\n\
##Order Time: 123000\n\
##CUSTOM PIZZA\n\
##Size: S\n\
##Toppings:\n\
##\t+ extra cheese\n\
##\t+ sausage\n\
##Price: $9.00\n\
##\n\
##----\n\
##SPECIALTY PIZZA\n\
##Size: S\n\
##Name: Carne-more\n\
##Price: $12.00\n\
##\n\
##----\n\
##TOTAL ORDER PRICE: $21.00\n\
##******\n"

