
#bar chart

import plotly.express as px

# Assuming 'Order Priority' is on the x-axis and 'Unit Price' is on the y-axis
x_column = 'Order Priority'
y_column = 'Unit Price'

# Limit the DataFrame to the first 10 rows (adjust as needed)
limited_dataframe = dataframe.head(10)

# Create a bar chart using Plotly Express
fig = px.bar(limited_dataframe, x=x_column, y=y_column, title='Limited Bar Chart Example', labels={'Unit Price': 'Average Unit Price'})

# Show the chart
fig.show()




#histogram

# Sample DataFrame
#data = {'Values': [25, 30, 15, 30, 40, 20, 25, 35, 45, 50, 55]}

#df = pd.DataFrame(data)

# Create a histogram using Plotly Express
#fig = px.histogram(df, x='Values', nbins=10, title='Histogram Example', labels={'Values': 'Count'})

# Show the chart
#fig.show()




#histogram

import plotly.express as px

# Assuming you want to create a histogram of the 'Unit Price' column
histogram_column = 'Order Priority'

# Limit the DataFrame to the first 100 rows (adjust as needed)
limited_dataframe = dataframe.head(50)

# Create a histogram using Plotly Express with the limited data
fig = px.histogram(limited_dataframe, x=histogram_column, title='Limited Histogram Example', labels={'Order Priority': 'Price'})

# Show the chart
fig.show()




#scatter plot

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





#pie chart

import plotly.express as px

# Assuming you want to create a pie chart of the 'Order Priority' column
pie_chart_column = 'Order Priority'

# Limit the DataFrame to the first 10 rows (adjust as needed)
limited_dataframe = dataframe.head(10)

# Create a pie chart using Plotly Express with the limited data
fig = px.pie(limited_dataframe, names=pie_chart_column, title='Limited Pie Chart Example', labels={'Order Priority': 'Priority Distribution'})

# Show the chart
fig.show()
