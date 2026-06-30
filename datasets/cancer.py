import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load LPG dataset
df = pd.read_csv(r"D:\India_lpg_dataset.csv")
print(df)
# Clean column names
df.columns = df.columns.str.strip()

# Print columns to confirm correct dataset
print("Columns in dataset:")
print(df.columns)

# Select correct LPG columns
df = df[['Year', 'Production_MMT', 'Imports_MMT', 'Price_INR']]

# Rename for easy use
df.columns = ['Year', 'Production', 'Imports', 'Price']

print(df.head())

# Plot LPG Price trend
plt.figure(figsize=(10,5))
sns.lineplot(x='Year', y='Price', data=df, marker='o')

plt.title("LPG Price Trend Over Years")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()