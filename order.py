from client import Client

class Order():
    def __init__(self, total_price, status):
        self.client = Client()
        self.total_price = total_price
        self.status = status