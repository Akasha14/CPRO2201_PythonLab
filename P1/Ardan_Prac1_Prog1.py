def get_valid_age():

    # Keep looping until return.
    while True:
        try:
            # Get age.
            age = int(input("Please entor your age: "))

            # If over 0, good age.
            if age > 0:
                return age
            
            # Age = 0, or negative.
            else:
                print("Age must be a positive number.")

        # Age = NaN
        except ValueError:
            print("Invalid. Entry must be a number!")

# Main program logic.
def main():
    age = get_valid_age()
    print(f"Your age is: {age}")

main()