from itertools import product
from typing import Type

from typing import TypeVar
from orderitem import Orderitem

class Order():
    def __init__(self, total_price, status, client):
        self.total_price = None
        self.status = status
        self.client = client

    def total_price(self, total_price: Orderitem):
        self.toal_price += total_price.unitary_price