from category import Category

class Product():
    def __init__ (self, name, description, date_fabrication, is_activate):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_activate = is_activate
        self.category = Category()