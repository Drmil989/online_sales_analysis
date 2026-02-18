from product import Product
from product_manager import ProductManager

# Kreiranje manager-a
manager = ProductManager()

# Dodavanje proizvoda
p1 = Product("Laptop", 1200, 5)
p2 = Product("Telefon", 800, 10)
p3 = Product("Slušalice", 150, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz proizvoda
manager.display_products()

# Ukupna vrednost
print("Ukupna vrednost inventara:", manager.total_inventory_value())

from cart import Cart

# Kreiranje korpe
cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

print("\nSadržaj korpe:")
cart.display_cart()

print("Ukupno za naplatu:", cart.calculate_total())
