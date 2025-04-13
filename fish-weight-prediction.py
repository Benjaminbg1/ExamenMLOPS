# %%
# Step 1 : import library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pickle



# %%
# Step 2 : import data
fish = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Fish.csv')

# %%
fish.head()

# %%
fish.info()

# %%
fish.describe()

# %%
# Step 3 : define target (y) and features (X)

# %%
fish.columns

# %%
y = fish['Weight']

# %%
X = fish[['Category','Height', 'Width', 'Length1',
       'Length2', 'Length3']]

# %%
# Step 4 : train test split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=20250410)

# %%
# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# %%
# Step 5 : select model
model = LinearRegression()

# %%
# Step 6 : train or fit model
model.fit(X_train,y_train)

# %%

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Se ha guardado model.pkl")

with open("features.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)
print("Se ha guardado features.pkl")

# %%
#model.intercept_

# %%
#model.coef_

# %%
# Step 7 : predict model
y_pred = model.predict(X_test)
print(f"Predicciones {y_pred}")
