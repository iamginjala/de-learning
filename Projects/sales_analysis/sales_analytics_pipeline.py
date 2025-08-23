import pandas as pd 
import os

cwd = os.getcwd()
full_path = os.path.join(cwd,'Projects','sales_analysis','sample_sales_data.csv')


## 1. Initial Exploration (pandas)

# Load your dataset into pandas.
df = pd.read_csv(full_path)

# Look at the first few rows to confirm structure.
# print(df.head())

# Check the number of rows and columns.
print(df.shape)
# check name of the columns
print(df.columns)

# Review data types for each column.
print(df.dtypes)

# Identify missing values across columns.
print(df.isna().sum())
# Look at unique values for categorical fields (region, sales rep, category).
regions = df['region'].unique()
represantive = df['sales_rep'].value_counts()
cate = df['category'].unique()
print(regions)
print(represantive)
print(cate)

# Verify numeric fields like quantity, unit price, and total sales for any negative or suspicious values.
print((df['quantity'] < 0).sum())
print((df['unit_price'] <= 0).sum())
print((df['total_sales'] < 0).sum())
df['total'] = df['quantity'] * df['unit_price']
print(df['total'].equals(df['total_sales']))
print(df[df['total'] != df['total_sales']])
# Make sure order_id looks unique.
print(df['order_id'].nunique())