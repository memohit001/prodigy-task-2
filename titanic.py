import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('train.csv')

# Data Cleaning
# Handling Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Data Type Corrections
df['Survived'] = df['Survived'].astype('category')

# Removing Duplicates
df.drop_duplicates(inplace=True)

# Exploratory Data Analysis (EDA)
# Initial Exploration
print(df.head())
print(df.isnull().sum())
print(df.describe())

# Data Visualization
# Survival by Sex
plt.figure(figsize=(10, 5))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.show()

# Survival by Passenger Class
plt.figure(figsize=(10, 5))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Passenger Class')
plt.show()

# Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', bins=30)
plt.title('Age Distribution of Survivors and Non-Survivors')
plt.show()

# Fare Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Fare', hue='Survived', multiple='stack', bins=30)
plt.title('Fare Distribution of Survivors and Non-Survivors')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
