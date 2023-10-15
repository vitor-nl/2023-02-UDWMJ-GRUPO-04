from orderitem import Orderitem

class Order():

  def __init__(self, status, client):
    self.total_price = 0
    self.status = status
    self.client = client

  def add_total_price(self, total_price: Orderitem):
    self.total_price += total_price.unitary_price * total_price.quantity
