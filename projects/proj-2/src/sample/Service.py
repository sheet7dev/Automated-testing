from src.sample.Storage import *


class Service:

    def __init__(self):
        self.storage = Storage()

    # tworzy klienta i zwraca true lub false i wyrzuca exc
    def addCustomer(self, customer):
        if self.storage.addCustomer(customer):
            return 'customer has been added'
        else:
            raise Exception('error occured')

    # zwraca true jesli usunieto lub false jesli go nie ma lub wystapil blad
    def deleteCustomer(self, customer_id):
        if self.storage.deleteCustomer(customer_id):
            return f'customer with id: {customer_id} deleted'
        else:
            raise Exception('error occured or customer with this id not exits')

    def getCustomer(self, customer_id):
        customers = self.storage.getCustomers()
        if isinstance(customers, list):
            for customer in customers:
                if customer.customer_id == customer_id:
                    return customer
            else:
                raise Exception('customer not exits')
        else:
            raise Exception('error occured')

    def addProduct(self, product):
        if self.storage.addProduct(product):
            return 'product has been added'
        else:
            raise Exception('error occured')

    def deleteProduct(self, product_id):
        if self.storage.deleteProduct(product_id):
            return f'product with id: {product_id} deleted'
        else:
            raise Exception('error occured or product with this id not exits')

    def getProduct(self, product_id):
        products = self.storage.getProducts()
        if isinstance(products, list):
            for product in products:
                if product.product_id == product_id:
                    return product
            else:
                raise Exception('product not exists')
        else:
            raise Exception('error occured')

    def addOrder(self, order):
        if self.storage.addOrder(order):
            return 'order has been added'
        else:
            raise Exception('error occured')

    def deleteOrder(self, order_id):
        if self.storage.deleteOrder(order_id):
            return f'order with id: {order_id} deleted'
        else:
            raise Exception('error occured or order with this id not exits')

    def getOrder(self, order_id):
        orders = self.storage.getOrders()
        if isinstance(orders,list):
            for order in orders:
                if order.order_id == order_id:
                    return order
            else:
                raise Exception('order not exists')
        else:
            raise Exception('error occured')

    def addProductToOrder(self, product_id, order_id):
        product = self.getProduct(product_id)
        order = self.getOrder(order_id)
        order.products.append(product)
        return order

    def deleteProductFromOrder(self, product_id, order_id):
        product = self.getProduct(product_id)
        order = self.getOrder(order_id)
        order.products.remove(product)
        return order

    def getCustomerOrders(self, customer_id):
        orders = self.storage.getOrders()
        customer_orders = []
        if isinstance(orders, list):
            for order in orders:
                if order.customer_id == customer_id:
                    customer_orders.append(order)
            return customer_orders
        else:
            raise Exception("error occured")
