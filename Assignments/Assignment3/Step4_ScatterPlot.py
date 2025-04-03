import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Plot the scatter plot with marker styles.
plt.scatter(csv_data['Sales'], csv_data['Profit'], color='green', edgecolor='black',  marker='x', s=200)

# Add labels and title.
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.title('Scatter Plot: Sales vs. Profit')

# Show the chart.
plt.show()