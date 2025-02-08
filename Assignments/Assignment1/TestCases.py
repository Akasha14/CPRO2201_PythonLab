from Product import *
from Sale import *
from Inventory import *

# Step 5

def testCases_func():

    # Step 5.1
    print("\n*TEST CASE 1* - Adding Products to inventory:")

    # Create an Inventory object.
    inventory = Inventory()
    # Create objects/instances.
    productShampoo = Product(product_id=101, name="Shampoo", price=5.99, stock_quantity=50)
    productLaptop = ElectronicsProduct(product_id=102, name="Laptop", price=899.99, stock_quantity=20, warranty_period=24)
    productMilk = PerishableProduct(product_id=103, name="Milk", price=2.49, stock_quantity=100, expiration_date="2025-02-15")
    # Adding objects to the inventory dictionary.
    inventory.add_product(productShampoo)
    inventory.add_product(productLaptop)
    inventory.add_product(productMilk)

    # Step 5.2
    print("\n*TEST CASE 2* - Selling Products and Reducing Stock Quantities:")

    sale1 = Sale(productShampoo, 3)    # Selling 3 shampoo.
    sale2 = Sale(productLaptop, 5)   # Selling 5 laptops.
    total1 = sale1.process_sale()
    total2 = sale2.process_sale()
    print(f"Total sale amount for shampoo: ${total1:.2f}")
    print(f"Total sale amount for Laptop: ${total2:.2f}")

    # Step 5.3
    print("\n*TEST CASE 3* - Listing Products and Displaying Product Details:")

    # List items.
    print("[Inventory List after sale:]")
    inventory.list_products()

    # Remove milk and list items.
    print("\n[Listing all products after removing milk:]")
    inventory.remove_product(103)
    inventory.list_products()

    # Update price and stock quantity then list items.
    print("\n[Updating price and stock quantity for products:]")
    productShampoo.update_price(6.49)
    productLaptop.update_price(849.99)
    productShampoo.update_stock(20)
    productLaptop.update_stock(10) 
    print("Listing all products after updates:")
    inventory.list_products()


    # Step 5.4
    print("\n*TEST CASE 4* - Handling Edge Cases:")

    # Removing non-existent product.
    print("[Attempted to remove a product with invalid ID (200):]")
    inventory.remove_product(200) 

    # Insufficent stock during sale.
    print("\n[Attempted to sell more shampoo than in stock.]")
    sale3 = Sale(productShampoo, 100) 
    total3 = sale3.process_sale()
    print(f"Total sale amount for shampoo: ${total3:.2f}")
    print("Listing all products after attempting to sell shampoo:")
    inventory.list_products()

    # Try negative price. 
    print("\n[Attempted to  insert negative price:]")
    productShampoo.update_price(-2.79)
    print("Listing all products after negative price:")
    inventory.list_products()
    


# Run test cases and view in console.
testCases_func()
