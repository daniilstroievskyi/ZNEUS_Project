import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




houses = pd.read_csv('houses.csv', sep=None, engine='python');
houses.name = "Houses"
print(houses.columns)


# Compute the correlation matrix
corr = houses.corr(numeric_only=True)

# Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,          # show correlation coefficients
    cmap="coolwarm",     # color map (can change to "viridis", "magma", etc.)
    fmt=".2f",           # format for numbers
    square=True,         # make cells square
    linewidths=0.5,      # add lines between cells
)
plt.title("Correlation Map", fontsize=14)
plt.show()

