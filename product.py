class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0  

    def __init__(self):
        ShoppingCart.total_carts += 1
        self.items = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} {product.product_name}(s) to cart.")
        else:
            print("Insufficient quantity in stock.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Removed {item[1]} {product.product_name}(s) from cart.")
                return
        print("Product not found in cart.")

    def display_cart(self):
        print("Cart Contents:")
        for item in self.items:
            print(f"{item[1]} x {item[0].product_name} = ${item[1] * item[0].price:.2f}")

    def calculate_total(self):
        total = sum(item[1] * item[0].price for item in self.items)
        return total


product1 = Product("Apple Watch", 299.99, 10)
product2 = Product("Samsung TV", 999.99, 5)
product3 = Product("Nike Shoes", 79.99, 20)


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart2.add_to_cart(product3, 3)
cart2.add_to_cart(product1, 1)
cart1.remove_from_cart(product2)


print("Cart 1 Contents:")
cart1.display_cart()
print("\nCart 2 Contents:")
cart2.display_cart()


print("\nCart 1 Total: $", cart1.calculate_total())
print("Cart 2 Total: $", cart2.calculate_total())

print("\nProduct Information:")
product1.display_product_info()
print("\n")
product2.display_product_info()
print("\n")
product3.display_product_info()