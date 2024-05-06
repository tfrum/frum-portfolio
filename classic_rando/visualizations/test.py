import matplotlib.pyplot as plt
import pandas as pd

# Dummy data for Canada's GDP from 2000 to 2010 (in billions of USD)
# This data is illustrative and may not be accurate
years = list(range(2000, 2011))
gdp = [912.9, 946.7, 978.8, 1043.0, 1092.6, 1134.4, 1286.1, 1423.7, 1474.8, 1352.3, 1613.5]

# Creating a pandas dataframe
df = pd.DataFrame({
    'Year': years,
    'GDP (in billions USD)': gdp
})

# Plotting the graph
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['GDP (in billions USD)'], marker='o', linestyle='-', color='b')
plt.title('Canada GDP from 2000 to 2010')
plt.xlabel('Year')
plt.ylabel('GDP (in billions USD)')
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()