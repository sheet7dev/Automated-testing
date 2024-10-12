class Order:
    def __init__(self, order_id, customer_id):
        if type(order_id) is not int:
            raise TypeError('order id must be an int')
        if type(customer_id) is not int:
            raise TypeError('order id must be an int')
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = []



