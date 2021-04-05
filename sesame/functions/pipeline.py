"""This is a script to store all methods used in this workflow."""
import pickle
import json
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from config import Config



class Pipeline:
    """Creating a class for all functions in the project."""


    def __init__(self):
        """Initializing the class."""
        pass


    def load_features(data=None):
        """Function to load features from directory."""
        data = pd.read_csv(str(Config.features_path / data))
        return data


    def calculate_r2(ground_truth=None, predictions=None):
        """Function to calculate coefficient of determination."""
        r2 = r2_score(ground_truth, predictions)
        r2 = round(r2, 3)
        return r2


    def calculate_rmse(ground_truth=None, predictions=None):
        """Function to calculate root mean squared error."""
        rmse = np.sqrt(mean_squared_error(
            ground_truth, predictions
        ))
        rmse = round(rmse, 3)
        return rmse


    def load_pickle(filename=None, funct=None):
        """Function load pickle file."""
        return pickle.load(open(
            str(Config.models_path / filename), funct
        ))


    def dump_pickle(model, filename=None, funct=None):
        """Function to save model to a pickle file."""
        return pickle.dump(model, open(
            str(Config.models_path / filename), funct
        ))
                
        
    def dump_dataset(dataset=None, data=None):
        """Function to save pandas DataFrame to csv file."""
        dataset.to_csv(str(Config.dataset_path / data), index=None)

    
    def dump_json(metric_1=None, metric_2=None):
        """Save metrics calculated to a json file."""
        with open(str(Config.metrics_path), 'w') as outfile:
            json.dump(
                dict(r_squared=metric_1, rmse=metric_2), outfile
            )

