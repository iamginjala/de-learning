import pandas as pd
import os
cwd = os.getcwd()
folder = os.path.join(cwd,'python_practice','Datasets','titanic') 
file = 'train.csv'
full_path = os.path.join(folder,file)
df = pd.read_csv(full_path)
### Basic Exploration

# # What are the number of rows and columns in the dataset?

# print(df.shape)

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

# GroupBy & Aggregation

# Calculate the average fare paid by each passenger class.
print(df.groupby('Pclass')['Fare'].mean())

# Find the survival rate by passenger class (Pclass).
print(df.groupby('Pclass')['Survived'].mean())

# Calculate the average age of passengers grouped by survival status (Survived).
print(df.groupby('Survived')['Age'].mean())
print(df.groupby(['Survived','Sex'])['Age'].mean())
# Find the number of siblings/spouses (SibSp) and parents/children (Parch) grouped by survival status.
# print(df.groupby('Survived')['SibSp'].sum())
# print(df.groupby('Survived')['Parch'].sum())
print(df.groupby('Survived')[['SibSp', 'Parch']].agg(['count', 'sum', 'mean']).round(2))
# For each embarkation port (Embarked), calculate the survival rate.
print(df.groupby('Embarked')['Survived'].mean())

## Pivot Tables
'''pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean',
 fill_value=None, margins=False, margins_name='All', dropna=True)
'''

# Create a pivot table showing survival rate by Pclass and Sex.
pt = pd.pivot_table(df,values='Survived',index=['Pclass','Sex'])
print(pt)

# Create a pivot table of average fare grouped by Pclass and Embarked.
pt2 = pd.pivot_table(df,values='Fare',index=['Pclass','Embarked'])
#or 
pt3 = pd.pivot_table(df,values='Fare',index='Pclass',columns='Embarked')
print(pt3)
# Create a pivot table of survival counts with margins (totals).
pt4 = pd.pivot_table(df,values='Survived',index='Sex',columns='Pclass',aggfunc='sum',margins=True)
print(pt4)
# Show the average age grouped by both Sex and Pclass using a pivot table.
pt5 = pd.pivot_table(df,values='Age',index=['Sex','Pclass'])
print(pt5)
pt6 = pd.pivot_table(df,values='Age',index='Sex',columns='Pclass')
print(pt6)