class Product:
    def __init__(self, product_id, name, value):
        if type(product_id) is not int:
            raise TypeError("product id must be an int")
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not float:
            raise TypeError("value must be a number")
        if value <= 0:
            raise ValueError("wrong value")
        self.product_id = product_id
        self.name = name
        self.value = value

