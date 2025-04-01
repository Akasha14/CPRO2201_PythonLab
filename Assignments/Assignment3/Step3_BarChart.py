import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Plotting the bar chart.
plt.bar(csv_data['Month'], csv_data['Sales'], color='#6495ED')  # Custom color.

# Add labels and title.
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Bar Chart')
# Rotate x-axis labels for better visibility.
plt.xticks(rotation=45) 

# Show the chart.
plt.show()