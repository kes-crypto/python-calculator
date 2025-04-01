import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset (Change filename accordingly)
    df = pd.read_csv("your_dataset.csv")
    
    # Display first few rows
    print("First 5 rows:")
    print(df.head())
    
    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Clean dataset (fill or drop missing values)
    df.fillna(df.mean(), inplace=True)  # Replace missing numerical values with mean
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Example grouping (change column names accordingly)
if 'Category' in df.columns and 'Value' in df.columns:
    group_means = df.groupby('Category')['Value'].mean()
    print("\nMean Value by Category:")
    print(group_means)

# Task 3: Data Visualization
plt.figure(figsize=(12, 6))

# Line Chart
if 'Date' in df.columns and 'Sales' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date is in datetime format
    df.plot(x='Date', y='Sales', kind='line', title='Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.show()

# Bar Chart
if 'Category' in df.columns and 'Sales' in df.columns:
    sns.barplot(x='Category', y='Sales', data=df)
    plt.title('Average Sales by Category')
    plt.show()

# Histogram
if 'Price' in df.columns:
    plt.hist(df['Price'], bins=20, color='blue', alpha=0.7)
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot
if 'Feature1' in df.columns and 'Feature2' in df.columns:
    sns.scatterplot(x='Feature1', y='Feature2', data=df)
    plt.title('Feature1 vs Feature2')
    plt.show()

print("\nAnalysis complete. Adjust column names and dataset path as needed.")
