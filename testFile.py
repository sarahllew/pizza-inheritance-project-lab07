from Pizza import *
from CustomPizza import *
from PizzaOrder import *
from SpecialtyPizza import *
from OrderQueue import *

# Pizza.py Tests
def test_Pizza():
    p1 = Pizza("S")
    p1.getPrice == 0.0
    p1.setPrice(20.00)
    p1.getPrice == 20.00
    p1.getSize == "S"
    p1.setSize == "M"
    p1.getSize == "M" 

# CustomPizza.py Tests
def test_CustomPizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n"
    cp1.addTopping("extra pepperoni")
    cp1.addTopping("extra peppers")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra pepperoni\n\t+ extra peppers\nPrice: $9.00\n"
    cp2 = CustomPizza("L")
    assert cp2.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n"
    cp2.addTopping("extra cheese")
    cp2.addTopping("pineapple")
    cp2.addTopping("chicken")
    assert cp2.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ pineapple\n\t+ chicken\nPrice: $15.00\n"
    

# SpecialtyPizza.py Tests
def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Spicy chicken")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: Spicy chicken\nPrice: $12.00\n"
    sp2 = SpecialtyPizza("L", "Hawaiian")
    assert sp2.getPizzaDetails() == "SPECIALTY PIZZA\nSize: L\nName: Hawaiian\nPrice: $16.00\n"

# PizzaOrder.py Tests
def test_PizzaOrder():
    o1 = CustomPizza("S")
    o1.addTopping("extra pepperoni")
    o1.addTopping("extra peppers")
    o2 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(113024)
    order.addPizza(o1)
    order.addPizza(o2)
    assert order.getTime() == 113024
    assert order.getOrderDescription() == "******\nOrder Time: 113024\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra pepperoni\n\t+ extra peppers\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n"

    o3 = SpecialtyPizza("L", "Veggie Deluxe")
    o4 = SpecialtyPizza("S", "Salami")
    order2 = PizzaOrder(123000)
    order2.addPizza(o3)
    order2.addPizza(o4)
    assert order2.getTime() == 123000
    assert order2.getOrderDescription() == "******\nOrder Time: 123000\nSPECIALTY PIZZA\nSize: L\nName: Veggie Deluxe\nPrice: $16.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Salami\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $28.00\n******\n"

# OrderQueue.py Tests
def test_OrderQueue():
    oq = OrderQueue() 
    o1 = CustomPizza("S")
    o1.addTopping("extra pepperoni")
    o1.addTopping("extra peppers")
    o2 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(113024)
    order.addPizza(o1)
    order.addPizza(o2)
    oq.addOrder(order)
    assert oq.processNextOrder() == "******\nOrder Time: 113024\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra pepperoni\n\t+ extra peppers\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n"
    oq2 = OrderQueue()
    o3 = SpecialtyPizza("L", "Veggie Deluxe")
    o4 = SpecialtyPizza("S", "Salami")
    order2 = PizzaOrder(123000)
    order2.addPizza(o3)
    order2.addPizza(o4)
    oq2.addOrder(order2)
    assert oq2.processNextOrder() == "******\nOrder Time: 123000\nSPECIALTY PIZZA\nSize: L\nName: Veggie Deluxe\nPrice: $16.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Salami\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $28.00\n******\n"
    



