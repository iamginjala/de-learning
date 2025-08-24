import pandas as pd 
import os
import sqlite3

cwd = os.getcwd()
full_path = os.path.join(cwd,'Projects','sales_analysis','sample_sales_data.csv')


## 1. Initial Exploration (pandas)

# Load your dataset into pandas.
df = pd.read_csv(full_path)

# Look at the first few rows to confirm structure.
# print(df.head())

# # Check the number of rows and columns.
# print(df.shape)
# # check name of the columns
# print(df.columns)

# # Review data types for each column.
# print(df.dtypes)

# # Identify missing values across columns.
# print(df.isna().sum())
# # Look at unique values for categorical fields (region, sales rep, category).
# regions = df['region'].unique()
# represantive = df['sales_rep'].value_counts()
# cate = df['category'].unique()
# print(regions)
# print(represantive)
# print(cate)

# # Verify numeric fields like quantity, unit price, and total sales for any negative or suspicious values.
# print((df['quantity'] < 0).sum())
# print((df['unit_price'] <= 0).sum())
# print((df['total_sales'] < 0).sum())
# df['total'] = df['quantity'] * df['unit_price']
# print(df['total'].equals(df['total_sales']))
# print(df[df['total'] != df['total_sales']])
# # Make sure order_id looks unique.
# print(df['order_id'].nunique())

## 2.Data Cleaning With Pandas
## droping records with duplicate order_id

df_cleaned = df.drop_duplicates(subset='order_id',keep='first').copy()

## removing extra spaces in the sales_rep column
df_cleaned['sales_rep'] = df_cleaned['sales_rep'].str.strip()

## converting category column into title case 
df_cleaned['category'] = df_cleaned['category'].str.title()

## handing missing vales filling with default values 
df_cleaned['region'] = df_cleaned['region'].fillna('Unknown')
df_cleaned['sales_rep'] = df_cleaned['sales_rep'].fillna('Unassigned')
df_cleaned['customer_id'] = df_cleaned['customer_id'].fillna('Guest')


## Numeric Validation Columns: quantity, unit_price, total_sales

# creating new column order_type with deafult values sale,refund based on quantity

df_cleaned['order_type'] = df_cleaned['quantity'].apply(lambda x:'Refund' if x < 0 else 'Sale')

df_cleaned['calculated_sales'] = df_cleaned['quantity'] * df_cleaned['unit_price']
df_cleaned['total_sales'] = df_cleaned['calculated_sales']

df_cleaned = df_cleaned.drop('calculated_sales',axis=1)

df_cleaned['corrected_date'] = pd.to_datetime(df_cleaned['order_date'],errors='coerce')

df_cleaned=df_cleaned.dropna(subset=['corrected_date'])

df_cleaned['order_date'] = df_cleaned['corrected_date']
# Remove the temporary corrected_date column since you no longer need it
df_cleaned = df_cleaned.drop('corrected_date', axis=1)

# Verify your cleaning worked
print("Final dataset info:")
print(f"Shape: {df_cleaned.shape}")
print(f"Missing values: {df_cleaned.isnull().sum().sum()}")
print(f"Duplicate order_ids: {df_cleaned['order_id'].duplicated().sum()}")
print(f"Date type: {df_cleaned['order_date'].dtype}")
print(f"Negative quantities: {(df_cleaned['quantity'] < 0).sum()}")

## 3. Database connection 

conn = sqlite3.connect('sales.db')

## creating sales data table in sales database
df_cleaned.to_sql('sales_data',conn,if_exists='replace',index=False)