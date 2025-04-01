import pandas as pd
import matplotlib.pyplot as plt

# Read csv into a pandas DataFrame.
csv_data = pd.read_csv('sales_dataset.csv')

# Print first five rows.
print("First five rows of the dataset:")
print(csv_data.head())

# Display basic statistics.
print("\nBasic statistics of the dataset:")
print(csv_data.describe())