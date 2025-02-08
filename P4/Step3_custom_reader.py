# Step 3

FILENAME = "Step1_system_logs.txt"


def user_input_gen_func(keyword):
    # Case insensitivity.
    keyword_lower = keyword.lower()

    # Open in read(r) mode.
    with open(FILENAME, "r") as file:
        for line in file:
            # Convert to lowercase to compare.
            if keyword_lower in line.lower():
                # Generator yield.
                yield line.strip()

# Menu
def main():
    print("\n------------------------------------")
    print("Example searches: INFO, WARNING, ERROR, DEBUG")
    # Custom user keyword.
    keyword = input("Please enter the word you would like to search for:")

    print(f"\nLines containing the keyword '{keyword}':")
    # Use generator function to search through lines.
    for line in user_input_gen_func(keyword):
        print("-", line)
    print()

main()