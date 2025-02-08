# Step 2

FILENAME = "Step1_system_logs.txt"
# Hardcoded keyword.
keyword = "ERROR"


def generator_func(keyword):
# Open in read(r) mode.
    with open(FILENAME, "r") as file:
        # Chech for keyword in each line of file.
        for line in file:
            if keyword in line:
                # Generator yield.
                yield line.strip()

# One file run.
print("\nLines containing the keyword 'ERROR':")
# Use generator function to search through lines.
for line in generator_func(keyword):
    print("-", line)
print()