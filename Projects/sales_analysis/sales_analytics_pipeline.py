import pandas as pd 
import os
import sqlite3

# cwd = os.getcwd()
# full_path = os.path.join(cwd,'Projects','sales_analysis','sample_sales_data.csv')


# ## 1. Initial Exploration (pandas)

# # Load your dataset into pandas.
# df = pd.read_csv(full_path)

# # Look at the first few rows to confirm structure.
# # print(df.head())

# # # Check the number of rows and columns.
# # print(df.shape)
# # # check name of the columns
# # print(df.columns)

# # # Review data types for each column.
# # print(df.dtypes)

# # # Identify missing values across columns.
# # print(df.isna().sum())
# # # Look at unique values for categorical fields (region, sales rep, category).
# # regions = df['region'].unique()
# # represantive = df['sales_rep'].value_counts()
# # cate = df['category'].unique()
# # print(regions)
# # print(represantive)
# # print(cate)

# # # Verify numeric fields like quantity, unit price, and total sales for any negative or suspicious values.
# # print((df['quantity'] < 0).sum())
# # print((df['unit_price'] <= 0).sum())
# # print((df['total_sales'] < 0).sum())
# # df['total'] = df['quantity'] * df['unit_price']
# # print(df['total'].equals(df['total_sales']))
# # print(df[df['total'] != df['total_sales']])
# # # Make sure order_id looks unique.
# # print(df['order_id'].nunique())

# ## 2.Data Cleaning With Pandas
# ## droping records with duplicate order_id

# df_cleaned = df.drop_duplicates(subset='order_id',keep='first').copy()

# ## removing extra spaces in the sales_rep column
# df_cleaned['sales_rep'] = df_cleaned['sales_rep'].str.strip()

# ## converting category column into title case 
# df_cleaned['category'] = df_cleaned['category'].str.title()

# ## handing missing vales filling with default values 
# df_cleaned['region'] = df_cleaned['region'].fillna('Unknown')
# df_cleaned['sales_rep'] = df_cleaned['sales_rep'].fillna('Unassigned')
# df_cleaned['customer_id'] = df_cleaned['customer_id'].fillna('Guest')


# ## Numeric Validation Columns: quantity, unit_price, total_sales

# # creating new column order_type with deafult values sale,refund based on quantity

# df_cleaned['order_type'] = df_cleaned['quantity'].apply(lambda x:'Refund' if x < 0 else 'Sale')

# df_cleaned['calculated_sales'] = df_cleaned['quantity'] * df_cleaned['unit_price']
# df_cleaned['total_sales'] = df_cleaned['calculated_sales']

# df_cleaned = df_cleaned.drop('calculated_sales',axis=1)

# df_cleaned['corrected_date'] = pd.to_datetime(df_cleaned['order_date'],errors='coerce')

# df_cleaned=df_cleaned.dropna(subset=['corrected_date'])

# df_cleaned['order_date'] = df_cleaned['corrected_date']
# # Remove the temporary corrected_date column since you no longer need it
# df_cleaned = df_cleaned.drop('corrected_date', axis=1)

# # Verify your cleaning worked
# # print("Final dataset info:")
# # print(f"Shape: {df_cleaned.shape}")
# # print(f"Missing values: {df_cleaned.isnull().sum().sum()}")
# # print(f"Duplicate order_ids: {df_cleaned['order_id'].duplicated().sum()}")
# # print(f"Date type: {df_cleaned['order_date'].dtype}")
# # print(f"Negative quantities: {(df_cleaned['quantity'] < 0).sum()}")

# ## 3. Database connection 

conn = sqlite3.connect('sales.db')

# ## creating sales data table in sales database
# df_cleaned.to_sql('sales_data',conn,if_exists='replace',index=False)

# ## Create a cursor object

# # Quick verification - check row count
cursor = conn.cursor()
# # cursor.execute("SELECT COUNT(*) FROM sales_data")
# # row_count = cursor.fetchone()[0]
# # print(f"📊 Rows in database: {row_count}")

# # Check the table structure that pandas created
# cursor.execute("PRAGMA table_info(sales_data)")
# columns = cursor.fetchall()
# print("\n📋 Table structure:")
# for col in columns:
#     print(f"  {col[1]} - {col[2]}")  # column name - data type

# Testing database 
# test_query = 'SELECT * FROM SALES_DATA LIMIT 5'
# test_result = pd.read_sql(test_query,conn)
# print('printing first 5 rows from the database')
# print(test_result)

### SQL Analysis
# Basic Questions:

# What are our total sales by month/quarter?
# total_sales_query  = "SELECT strftime('%Y-%m', order_date) AS year_month,sum(total_sales) from sales_data " \
#                      "Group by year_month order by year_month"

# total_sales_result = pd.read_sql(total_sales_query,conn)
# print('total sales by month ')
# print(total_sales_result)
# Which products sell the most?
# most_selling_query = "SELECT product_name, SUM(quantity) AS total_quantity_sold FROM sales_data " \
#                     "GROUP BY product_name ORDER BY total_quantity_sold DESC "
# most_selling_result =  pd.read_sql(most_selling_query,conn)
# print(most_selling_result)
# How do regions compare in performance?
# reg_perf = "SELECT region,strftime('%Y' ,order_date) as year,sum(total_sales)" \
#             "from sales_data group by 1,2 order by 2"
# reg_perf_result = pd.read_sql(reg_perf,conn)
# print(reg_perf_result)

# Who are our top-performing sales reps?
# top_performer = "SELECT sales_rep, sum(total_sales) as tot_sal from sales_data " \
#                 "Group by sales_rep order by tot_sal desc"
# top_performer_result = pd.read_sql(top_performer,conn)
# print(top_performer_result) 

# Intermediate Questions:

# What's the average order value by category?
# avg_order_query = "select category,strftime('%Y', order_date) as year,avg(total_sales) as avg_value from sales_data" \
#                   " Group by 1,2 order by avg_value desc"
# avg_order_query_result = pd.read_sql(avg_order_query,conn)
# print(avg_order_query_result)
# Which customers buy the most frequently?
cust_query = "SELECT CUSTOMER_ID ,count(*) AS PURCHASE_COUNT FROM sales_data " \
"WHERE customer_id != 'Guest' GROUP BY customer_id ORDER BY PURCHASE_COUNT DESC"
cust_query_result = pd.read_sql(cust_query,conn)
print(cust_query_result)
# Are there seasonal patterns in our sales?
# What's the breakdown of sales vs refunds?

# Advanced Questions:

# Which product combinations are often bought together?
# How has sales performance trended over time?
# What's the customer lifetime value by region?