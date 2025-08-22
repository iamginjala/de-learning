import pandas as pd
import os
cwd = os.getcwd()
folder = os.path.join(cwd,'python_practice','Datasets','titanic') 
file = 'train.csv'
full_path = os.path.join(folder,file)
df = pd.read_csv(full_path)
print(df.head())
### Basic Exploration

# What are the number of rows and columns in the dataset?


# How many passengers survived and how many did not?

# What is the average age of passengers?

# What is the distribution of passengers by class (Pclass)?

# What is the survival rate for male vs female passengers?