import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

sales = csv_data['Sales']

# Plot the Histogram with 5 bins, and border styling.
plt.hist(sales, bins=5, edgecolor='black', linewidth=1.5, color='blue')

# Add labels and title.
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.title('Sales Distribution Histogram')

# Show the chart.
plt.show()