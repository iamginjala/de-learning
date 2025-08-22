import pandas as pd
import os
cwd = os.getcwd()
folder = os.path.join(cwd,'python_practice','Datasets','titanic') 
file = 'train.csv'
full_path = os.path.join(folder,file)
df = pd.read_csv(full_path)
### Basic Exploration

# What are the number of rows and columns in the dataset?

print(df.shape)

# what are the column names 

print(df.columns)

# How many passengers survived and how many did not?

total = df['Survived'].count()
print(f'Survived passengers: {df["Survived"].sum()}')
print(f'not survived passengers: {total-df["Survived"].sum()}')

# What is the average age of passengers?

avg_age = df['Age'].mean()
print(avg_age)
# What is the distribution of passengers by class (Pclass)?

print(df['Pclass'].value_counts())
# What is the survival rate for male vs female passengers?

survial_rate = pd.pivot_table(df,values='Survived',index='Sex',aggfunc='mean')
print(survial_rate)

# or using group by

survival = df.groupby('Sex')['Survived'].mean()
print(survival)