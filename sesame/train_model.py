'''This is a script to train a model with a variety of estimators.'''
from sklearn.ensemble import RandomForestRegressor
from config import Config
from functions import Pipeline as pp

# Creating a path to save our model
Config.models_path.mkdir(parents=True, exist_ok=True)

# Loading the training and testing features into a pandas DataFrame
x_train = pp.load_features(data='train_features.csv')
y_train = pp.load_features(data='train_target.csv')

# Instantiating and fitting the algorithm
model = RandomForestRegressor(n_estimators=9000)
model = model.fit(x_train, y_train.to_numpy().ravel())

# Saving the model into a pickle file
pp.dump_pickle(model, filename='model.pickle', funct='wb')
