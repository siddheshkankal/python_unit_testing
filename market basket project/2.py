import unittest
from product import Product
 
 
class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product(name="milk", price=3.0)
 
    def test_get_product_name(self) -> None:
        self.assertEqual(self.product.name, "milk")
 
    def test_get_product_price(self) -> None:
        self.assertEqual(self.product.price, 3.0)
 
    def test_get_quantity(self) -> None:
        self.assertEqual(self.product.quantity, 1)
 
    def test_repr_method(self) -> None:
        self.assertEqual(
            repr(self.product),
            "Product(name='milk', price=3.0, quantity=1)",
            "Product's __repr__ method did not return expected result"
        )