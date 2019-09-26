class Flower:
    def __init__(self, name=None, nr_petals=None, price=None):
        self.name = name
        self.nr_petals = nr_petals
        self.price = price
        assert type(name) == str, 'Expected string type for name'
        assert type(nr_petals) == int
        assert type(price) == float
    
    def set_name(self, new_name):
        self.name = new_name

    def set_nr_petals(self, new_nr_petals):
        self.name = new_nr_petals

    def get_name(self):
        return print(self.name)

    def get_nr_petals(self):
        return print(self.nr_petals)

    def get_price(self):
        return print(self.price)


