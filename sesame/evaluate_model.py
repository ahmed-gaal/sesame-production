'''This is a script to evaluate the accuracy of the model created earlier.'''
import pandas as pd
from config import Config
from functions.pipeline import Pipeline as pp

# Loading in our test data for evaluation
x_test = pd.read_csv(str(Config.features_path / 'test_features.csv'))
y_test = pd.read_csv(str(Config.features_path / 'test_target.csv'))

# Loading in the trained model
model = pp.load_pickle(filename='model.pickle', funct='rb')

# Performing predictions on the trained model
y_pred = model.predict(x_test)

# Calculating metrics for the model (root Mean squared error and R²)
r2 = pp.calculate_r2(ground_truth=y_test, predictions=y_pred)
rmse = pp.calculate_rmse(ground_truth=y_test, predictions=y_pred)

# Saving our results in a JSON file
pp.dump_json(metric_1=r2, metric_2=rmse)
