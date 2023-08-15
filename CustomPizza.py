from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppingsList = []
        if size == "S":
            self.price = 8.00
        elif size == "M":
            self.price = 10.00
        else:
            self.price = 12.00

    def addTopping(self, topping):
        self.toppingsList.append(topping)
        if self.size == "S":
            self.price += 0.50
        elif self.size == "M":
            self.price += 0.75
        else:
            self.price += 1.00

    def getPizzaDetails(self):
        if len(self.toppingsList) == 0:
            return "CUSTOM PIZZA\nSize: {}\nToppings:\nPrice: ${:.2f}\n".format(Pizza.getSize(self),self.price)
        else:
            toppings = ""
            for i in self.toppingsList:
                toppings += "\t" + "+ " + i + "\n"
            return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}\nPrice: ${:.2f}\n".format(Pizza.getSize(self),toppings[:-1],self.price)
                
##cp2 = CustomPizza("L")
##assert cp2.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n"      


##cp1 = CustomPizza("S")
##assert cp1.getPizzaDetails() == \
##"CUSTOM PIZZA\n\
##Size: S\n\
##Toppings:\n\
##Price: $8.00\n"

##cp2 = CustomPizza("L")
##cp2.addTopping("extra cheese")
##cp2.addTopping("sausage")

##assert cp2.getPizzaDetails() == \
##"CUSTOM PIZZA\n\
##Size: L\n\
##Toppings:\n\
##\t+ extra cheese\n\
##\t+ sausage\n\
##Price: $14.00\n"


        
        
        
