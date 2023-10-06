import client

class Order(client.Client):
    def __init__(self, first_name, last_name, addres, cell_phone, email, gender, total_price, status):
        super().__init__(first_name, last_name, addres, cell_phone, email, gender)