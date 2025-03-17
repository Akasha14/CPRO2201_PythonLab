from .addition import addition
from .subtraction import subtraction
from .multiplication import multiplication

# Prompt user to choose an operation.
def calculateMenu():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        userChoice = input("Enter choice (1/2/3/4): ")

        if userChoice == "4":
            print("Exiting calculator!")
            break  # Exit the loop

        if userChoice not in ("1", "2", "3"):
            print("Invalid choice! Please enter a valid option.")
            continue  # Restart the loop

        # Take 2 decimal numbers from the user.
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue  # Restart the loop if input is invalid

        # Perform calculation based on user inputs.
        if userChoice == "1":
            result = addition(num1, num2)
            operation = "Addition"
        elif userChoice == "2":
            result = subtraction(num1, num2)
            operation = "Subtraction"
        else:
            result = multiplication(num1, num2)
            operation = "Multiplication"

        # Print operation type and result.
        print(f"{operation} Result: {result}")