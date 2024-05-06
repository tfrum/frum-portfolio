import pandas as pd
import matplotlib.pyplot as plt

# All dummy data.
gdp =   (1012.65, 1052.10, 1090.00, 1120.30, 1152.40, 1187.80, 1225.50, 1265.40, 1242.30, 1200.00, 1230.70)
years = range(2000, 2011)

df = pd.DataFrame({"Year": years, "GDP": gdp})

# We're trying to make time series data out of our year column.
df.set_index('Year', inplace=True)
print(df)

# create a plot
df.plot(kind='line')
# populate the plot legends
plt.title('Canada GDP 2000-2010')
plt.xlabel('GDP')
plt.ylabel('Year')

# show it
plt.show()
