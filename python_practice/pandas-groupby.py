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

# # How many passengers survived and how many did not?

# total = df['Survived'].count()
# print(f'Survived passengers: {df["Survived"].sum()}')
# print(f'not survived passengers: {total-df["Survived"].sum()}')

# # What is the average age of passengers?

# avg_age = df['Age'].mean()
# print(avg_age)
# # What is the distribution of passengers by class (Pclass)?

# print(df['Pclass'].value_counts())
# # What is the survival rate for male vs female passengers?

# survial_rate = pd.pivot_table(df,values='Survived',index='Sex',aggfunc='mean')
# print(survial_rate)

# # or using group by

# survival = df.groupby('Sex')['Survived'].mean()
# print(survival)

## GroupBy & Aggregation

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