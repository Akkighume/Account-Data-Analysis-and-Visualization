import matplotlib.pyplot as plt

# Assuming 'Unit Price' is on the x-axis and 'Shipping Cost' is on the y-axis
x_column = 'Unit Price'
y_column = 'Shipping Cost'

# Limit the DataFrame to the first 100 rows (adjust as needed)
limited_data = dataframe.head(30)

# Create scatter plot with the limited data
plt.scatter(limited_data[x_column], limited_data[y_column], alpha=0.5)
plt.title('Scatter Plot of Unit Price vs Shipping Cost (Limited to 30 rows)')
plt.xlabel('Unit Price')
plt.ylabel('Shipping Cost')
plt.show()
