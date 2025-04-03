import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Data for Pie Chart
pie_months = csv_data['Month']
pie_sales = csv_data['Sales']

bar_colors = ['green', 'blue', 'yellow', 'red', 
              'purple', 'orange', 'cyan', 'magenta', 
              'pink', 'brown', 'gray', 'teal']

# Plot the Pie Chart with percentages , month labels and colours.
plt.pie(pie_sales, labels=pie_months, autopct='%1.1f%%', colors=bar_colors)

plt.title('Pie Chart: Sales Contribution per Month')
plt.show()
