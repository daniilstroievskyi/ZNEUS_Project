import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




houses = pd.read_csv('houses.csv', sep=None, engine='python');
houses.name = "Houses"
print(houses.columns)

