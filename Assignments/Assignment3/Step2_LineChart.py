import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Plot the line chart.
plt.plot(csv_data['Month'], csv_data['Sales'])

# Add labels and title.
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Trend')
# Add grid.
plt.grid(True)
# Rotate x axis labels for better visibility.
plt.xticks(rotation=45)
# Create space underneath the plot, to see x axis label.
plt.subplots_adjust(bottom=0.2)

# Display the chart.
plt.show()