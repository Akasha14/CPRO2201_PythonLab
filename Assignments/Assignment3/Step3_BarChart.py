import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

bar_colors = ['green', 'blue', 'yellow', 'red', 
              'purple', 'orange', 'cyan', 'magenta', 
              'pink', 'brown', 'gray', 'teal']

# Plot the bar chart using custom color scheme.
plt.bar(csv_data['Month'], csv_data['Sales'], color=bar_colors)

# Add labels and title.
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Bar Chart: Monthly Sales')
# Rotate x-axis labels for better visibility.
plt.xticks(rotation=45) 

# Show the chart.
plt.show()