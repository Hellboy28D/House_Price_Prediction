from utils import *
from preprocess import *

# Splitting data and target
X = house_price_data_frame.drop(['price'], axis=1)
Y = house_price_data_frame['price']

# Create encoder
encoder = LabelEncoder()

# Convert text columns into numeric values
X['date'] = encoder.fit_transform(X['date'])
X['street'] = encoder.fit_transform(X['street'])
X['city'] = encoder.fit_transform(X['city'])
X['statezip'] = encoder.fit_transform(X['statezip'])
X['country'] = encoder.fit_transform(X['country'])

print(X.head())

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=2
)

print(X.shape, X_train.shape, X_test.shape)

# Train model
model = XGBRegressor()

model.fit(X_train, Y_train)

print("Model trained successfully")