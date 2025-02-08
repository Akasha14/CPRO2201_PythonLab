from Product import *

# Step 3

class Sale:
    # Accept product object, and quantity to sell.
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


    def process_sale(self):
        # Use Product is_in_stock method.
        if self.product.is_in_stock(self.quantity):
            # Use product sell method to reduce stock and get total sale amount.
            total_sale_amount = self.product.sell(self.quantity)
            return total_sale_amount
        else:
            # If not enough stock, print error message and return 0.
            print(f"Error: Not enough stock for {self.product.name}.")
            return 0