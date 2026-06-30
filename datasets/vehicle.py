import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Indian_Traffic_Violations.csv")
df = df[['Violation_Type', 'Fine_Amount', 'Location', 'Vehicle_Type', 'Driver_Gender']]
df.columns = ['Violation', 'Fine', 'Place', 'Vehicle', 'Gender']

print(df.head())
print(df.describe())

sns.barplot(x='Violation', y='Fine', data=df, hue="Violation")
plt.xticks(rotation=45)
plt.show()