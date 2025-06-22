from datetime import datetime

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class StockChange:
    def __init__(self, productId, delta):
        self.productId = productId
        self.delta = delta
        self.timestamp = self.get_timestamp()

    @staticmethod
    def get_timestamp():
        return datetime.utcnow().isoformat()
