import pandas as pd 
import os

cwd = os.getcwd()
full_path = os.path.join(cwd,'Projects','sales_analysis','sample_sales_data.csv')


## 1. Initial Exploration (pandas)

# Load your dataset into pandas.
df = pd.read_csv(full_path)

# Look at the first few rows to confirm structure.
print(df.head())

# Check the number of rows and columns.

# Review data types for each column.

# Identify missing values across columns.

# Look at unique values for categorical fields (region, sales rep, category).

# Verify numeric fields like quantity, unit price, and total sales for any negative or suspicious values.

# Make sure order_id looks unique.