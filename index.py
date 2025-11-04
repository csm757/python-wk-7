# load and dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset using sklearn
try:
    iris_data = load_iris()
    # Create DataFrame
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = iris_data.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: File not found. Please check the dataset path.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

# Display the first few rows
print("📄 First 5 rows of the dataset:")
print(df.head())

# Check data info
print("\nℹ️ Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔍 Missing values:")
print(df.isnull().sum())

# Since Iris dataset has no missing values, we skip cleaning.
# But let's show how you'd handle missing data:
df.fillna(df.mean(numeric_only=True), inplace=True)

#DATA ANALYSIS
# Basic statistics
print("\n📈 Basic Statistics:")
print(df.describe())

# Group by species and compute the mean of numeric columns
print("\n📊 Average Measurements by Species:")
group_means = df.groupby('species').mean(numeric_only=True)
print(group_means)

# Insights
print("\n💡 Observations:")
print("- Setosa has the smallest petal measurements.")
print("- Virginica has the largest petals and sepals on average.")
print("- Versicolor sits between setosa and virginica in most features.")



# Visualize the data#
# Combined graphs for Iris dataset
import matplotlib.pyplot as plt
import seaborn as sns

# Use a simple style
sns.set_style("whitegrid")

# Create 4 plots in one figure
fig, ax = plt.subplots(2, 2, figsize=(13, 9))

# Line Chart - Cumulative Petal Length
ax[0, 0].plot(df['petal length (cm)'].cumsum(), color='green')
ax[0, 0].set_title('Cumulative Petal Length')
ax[0, 0].set_xlabel('Index')
ax[0, 0].set_ylabel('Cumulative Value')

# Bar Chart - Average Petal Length per Species
sns.barplot(x=group_means.index, y=group_means['petal length (cm)'], ax=ax[0, 1], color='skyblue')
ax[0, 1].set_title('Average Petal Length per Species')
ax[0, 1].set_xlabel('Species')
ax[0, 1].set_ylabel('Avg Petal Length (cm)')

# Histogram - Sepal Length
sns.histplot(df['sepal length (cm)'], bins=12, kde=True, ax=ax[1, 0], color='orange')
ax[1, 0].set_title('Distribution of Sepal Length')
ax[1, 0].set_xlabel('Sepal Length (cm)')
ax[1, 0].set_ylabel('Count')

# Scatter Plot - Sepal vs Petal Length
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', ax=ax[1, 1])
ax[1, 1].set_title('Sepal vs Petal Length')
ax[1, 1].set_xlabel('Sepal Length (cm)')
ax[1, 1].set_ylabel('Petal Length (cm)')

# Adjust layout so plots don’t overlap
plt.tight_layout()
plt.show()

