from utils import *

# Import dataset
house_price_data_frame = pd.read_csv(
    "data (1).csv"
)

# First 5 rows
print(house_price_data_frame.head())

# Shape of dataset
print(house_price_data_frame.shape)

# Check missing values
print(house_price_data_frame.isnull().sum())

# Dataset information
print(house_price_data_frame.info())

# Statistical summary
# Statistical measure of dataset
print(house_price_data_frame.describe())

# Select only numerical columns
numeric_data = house_price_data_frame.select_dtypes(
    include=['number']
)

# Correlation matrix
correlation = numeric_data.corr()

print(correlation)

# Heatmap
plt.figure(figsize=(10,10))

sns.heatmap(
    correlation,
    cbar=True,
    square=True,
    fmt='.1f',
    annot=True,
    annot_kws={'size':8}
)

plt.show()

