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


    def load_features(self, data=None):
        """Function to load features from directory."""
        data = pd.read_csv(str(Config.features_path / self.data))
        return data


    def calculate_r2(self, ground_truth=None, predictions=None):
        """Function to calculate coefficient of determination."""
        r2 = r2_score(self.ground_truth, self.predictions)
        return r2


    def calculate_rmse(self, ground_truth=None, predictions=None):
        """Function to calculate root mean squared error."""
        rmse = np.sqrt(mean_squared_error(
            self.ground_truth, self.predictions
        ))
        return rmse


    def load_pickle(self, filename=None, funct=None):
        """Function load pickle file."""
        return pickle.load(open(
            str(Config.models_path / self.filename), self.funct
        ))


    def dump_pickle(self, model, filename=None, funct=None):
        """Function to save model to a pickle file."""
        return pickle.dump(self.model, open(
            str(Config.models_path / self.filename), self.funct
        ))
                
        
    def dump_dataset(dataset=None, data=None):
        """Function to save pandas DataFrame to csv file."""
        dataset.to_csv(str(Config.dataset_path / data), index=None)

    
    def dump_json(self, metric_1=None, metric_2=None):
        """Save metrics calculated to a json file."""
        with open(str(Config.metrics_path), 'w') as outfile:
            json.dump(
                dict(r_squared=self.metric_1, rmse=self.metric_2), outfile
            )
