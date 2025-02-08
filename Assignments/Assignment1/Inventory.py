from Product import *
from Sale import *

# Step 4

class Inventory:

    def __init__(self):
        # Dictionary to store products {product id: product}.
        self.product_dict = {}

    def add_product(self, product):
        # Add product to dictionary with product id as key.
        self.product_dict[product.product_id] = product
        print(f"Product {product.name} added to inventory. (Qty: {product.stock_quantity})")

    def remove_product(self, product_id):
        if product_id in self.product_dict:
            # Remove from dictionary by product_id.
            removed_product = self.product_dict.pop(product_id)
            print(f"Product {removed_product.name} removed from inventory.")
        else:
            # Product Id not found.
            print(f"Product with ID {product_id} not found in inventory.")

    def list_products(self):
        # If empty.
        if not self.product_dict:
            print("No products in inventory.")
        else:
            # List all in dictionary.
            for product in self.product_dict.values():
                # Call any version of get_product_details.
                print(product.get_product_details()) 
