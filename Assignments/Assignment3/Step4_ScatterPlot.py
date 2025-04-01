import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('sales_dataset.csv')

plt.scatter(csv_data['Sales'], csv_data['Profit'], 
            color='green', edgecolor='black',  marker='x')

# Add labels and title.
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.title('Sales vs. Profit Scatter Plot')

# Show the plot
plt.show()