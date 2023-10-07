import category
class product():
    def __init__ (self, name_description, date_fabrication, is_activate):
        self.name_description = name_description
        self.date_fabrication = date_fabrication
        self.is_activate = is_activate
        self.category = category()