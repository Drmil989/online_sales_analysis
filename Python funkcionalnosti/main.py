from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Gaming Laptop", 1200, 5)
p2 = Product("Telefon", 800, 10)
p3 = Product("Slušalice", 150, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

print("\nSadržaj korpe:")
cart.display_cart()

print("Ukupno za naplatu:", cart.calculate_total())

