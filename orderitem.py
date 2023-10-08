from order import Order 
from product import Product

class Orderitem():
    def __init__(self, quantity, unitary_price):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = Order()
        self.product = Product()
        