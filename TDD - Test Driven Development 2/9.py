class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )
        self.price = price