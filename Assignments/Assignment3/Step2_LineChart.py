import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Plotting the line chart.
plt.plot(csv_data['Month'], csv_data['Sales'])

# Adding labels and title.
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Trend')
# Add grid.
plt.grid(True)
# Rotate x axis labels to make readable.
plt.xticks(rotation=45)

# Display the chart.
plt.show()