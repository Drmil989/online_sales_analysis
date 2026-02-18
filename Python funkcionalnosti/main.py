from product import Product
from product_manager import ProductManager

# Kreiranje manager-a
manager = ProductManager()

# Dodavanje proizvoda
p1 = Product("Gaming Laptop", 1200, 5)
p2 = Product("Telefon", 800, 10)
p3 = Product("Slušalice", 150, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz proizvoda
manager.display_products()


