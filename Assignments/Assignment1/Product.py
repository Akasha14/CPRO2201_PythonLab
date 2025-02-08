# Step 1

class Product:

    # Constructor (Step 1.1).
    def __init__(self, product_id: int, name: str, price: float, stock_quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price 
        self.stock_quantity = stock_quantity

    # Step 1.2
    def update_price(self, new_price):
        if new_price < 0:
            print("Error: Price cannot be negative.")
            return
        else:
            self.price = new_price

    def update_stock(self, quantity):
        # Add quantity to stock.
        self.stock_quantity += quantity

    def is_in_stock(self, quantity):
        # True if in stock.
        return self.stock_quantity >= quantity
    
    def sell(self, quantity):
        # Reduce stock.
        self.stock_quantity -= quantity
        # Calculate total sale amount.
        return quantity * self.price
    
    def get_product_details(self):
        return (
            f"Name: {self.name}, "
            f"Price: ${self.price:.2f}, "
            f"Stock Quantity: {self.stock_quantity}"
        )


# Step 2.1
class ElectronicsProduct(Product):

    def __init__(self, product_id, name, price, stock_quantity, warranty_period):
        # Constructor (use original - super(), add warranty_period).
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty_period = warranty_period

    # Override parent method.
    def get_product_details(self):
        return (
            f"Name: {self.name}, "
            f"Price: ${self.price:.2f}, "
            f"Stock Quantity: {self.stock_quantity}, "
            f"Warranty Period: {self.warranty_period}" # Add this.
        )
    

# Step 2.2
class PerishableProduct(Product):

    def __init__(self, product_id, name, price, stock_quantity, expiration_date):
        # Constructor (use original - super(), add expiration_date).
        super().__init__(product_id, name, price, stock_quantity)
        self.expiration_date = expiration_date 
    
    # Override parent method.
    def get_product_details(self):
        return (
            f"Name: {self.name}, "
            f"Price: ${self.price:.2f}, "
            f"Stock Quantity: {self.stock_quantity}, "
            f"Expiration Date: {self.expiration_date}" # Add this.
        )