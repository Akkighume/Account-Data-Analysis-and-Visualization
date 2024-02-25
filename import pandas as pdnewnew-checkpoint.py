import pandas as pd 
import json 
df = pd.read_json("C:\Users\HP\newjson.py")
df

import duckdb

# Connect to DuckDB
connection = duckdb.connect(database=':memory:', read_only=False)

# Execute queries or perform database operations
result = connection.execute("SELECT * FROM newjson.py")
dataframe = result.fetchdf()
dataframe

# Close the connection when done
connection.close()
