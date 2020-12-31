'''
This is a script to train a model with a variety of estimators
'''
import pickle
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from config import Config
from functions import Pipeline as pp

# Creating a path to save our model
Config.models_path.mkdir(parents=True, exist_ok=True)

# Loading the training and testing features into a pandas DataFrame
x_train = pp.load_features(data='train_features.csv')
y_train = pp.load_features(data='train_target.csv')

# Instantiating and fitting the algorithm
model = AdaBoostRegressor(learning_rate=1.0, loss='square',
                  n_estimators=50, random_state=42)
model = model.fit(x_train, y_train.to_numpy().ravel())

# Saving the model into a pickle file
pp.dump_pickle(model, filename='model.pickle', funct='wb')
