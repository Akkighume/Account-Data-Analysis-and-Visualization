import duckdb
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import matplotlib as mpl  
import matplotlib.pyplot as plt

# Set up a DuckDB connection
con = duckdb.connect(database=':memory:', read_only=False)

json_file_path = "C:/Users/HP/newjson.py"

# Table
selected_columns = ['Region', 'Sales', 'Profit', 'Discount', 'City', 'OrderPriority', 'StateorProvince', 'ShipMode', 'CustomerSegment' ,'ProductCategory', 'Country', 'ProductContainer']  # Correct the column names here
columns_str = ', '.join(selected_columns)

# Use double curly braces to include the file path in the SQL string
con.execute(f'CREATE TABLE json_data AS SELECT {columns_str} FROM READ_JSON_AUTO(\'{json_file_path}\');')

# Fetch data from DuckDB and convert it into a Pandas DataFrame
result = con.execute(f'SELECT * FROM json_data;')
columns = [col[0] for col in result.description]
data = result.fetchall()

df = pd.DataFrame(data, columns=columns)

# Display the DataFrame
print(df)

#Data Visualisation

data0 = df.groupby('StateorProvince')['Profit'].count().reset_index()
data0

#Figure-1
fig1 = px.scatter(df, x='StateorProvince', y='Profit', title='Scatter Plot of Profit by State or Province', 
                 labels={'Profit': 'Profit'}, color='StateorProvince', 
                 hover_data=['City', 'Sales', 'Discount', 'OrderPriority', 'ShipMode', 'CustomerSegment', 'ProductCategory'])
fig1.show()


#Figure-2
fig2 = px.bar(data0,x='StateorProvince', y='Profit', 
              title='State or Province vs Profit') 
fig2.update_layout(xaxis_title='State or Province', yaxis_title='Profit')
fig2.show()

 
#Figure-3
fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=df['CustomerSegment'], nbinsx=30, marker_color='skyblue'))
fig3.update_layout(title='Histogram of Customer Segment', xaxis=dict(title='CustomerSegment'), yaxis=dict(title='Frequency'))
fig3.show()


#Figure-4
data2 = df.groupby('Region')['Sales'].count().reset_index()
data2

fig4= px.bar(data2,x='Region', y='Sales', 
              title='Region vs Sales') 
fig4.update_layout(xaxis_title='Region', yaxis_title='Sales')
fig4.show()