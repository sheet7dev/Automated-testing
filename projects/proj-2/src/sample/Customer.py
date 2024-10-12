class Customer:
    def __init__(self, customer_id, name, email):
        if type(customer_id) is not int:
            raise TypeError("customers id must be an int")
        if type(name) is not str:
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name cannot be an empty string")
        self.customer_id = customer_id
        self.name = name
        self.email = email




