import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

# Set up and adjust figure layout.
plt.figure(figsize=(12, 10))
plt.suptitle('Subplots: Multiple Charts', fontsize=20, fontweight='bold')

####################### Line Chart #######################

# Plot in the subplot.
plt.subplot(2, 2, 1)

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

####################### Bar Chart #######################

# Plot in the subplot.
plt.subplot(2, 2, 2)

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

####################### Scatter Plot #######################

# Plot in the subplot.
plt.subplot(2, 2, 3)

# Plot the scatter plot with marker styles.
plt.scatter(csv_data['Sales'], csv_data['Profit'], color='green', edgecolor='black',  marker='x', s=200)

# Add labels and title.
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.title('Scatter Plot: Sales vs. Profit')

####################### Pie Chart #######################

# Plot in the subplot.
plt.subplot(2, 2, 4)

# Data for Pie Chart
pie_months = csv_data['Month']
pie_sales = csv_data['Sales']


# Plot the Pie Chart with percentages , month labels and colours.
plt.pie(pie_sales, labels=pie_months, autopct='%1.1f%%', colors=bar_colors)

plt.title('Pie Chart: Sales Contribution per Month')

####################### Display #######################

# Adjust spacing.
plt.tight_layout(pad=3)

# Show the plots
plt.show()