class Laptop:
    def __init__(self, brand, model, price):
        if not isinstance(brand, str):
            raise TypeError(
                'The brand attribute must be string.'
            )
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )
        if not price > 0:
            raise ValueError(
                'The price attribute must be positive.'
            )
        self.price = price