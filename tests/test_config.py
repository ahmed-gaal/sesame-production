import unittest
from pathlib import Path
from sesame.config import Config

class TestConfigFile(unittest.TestCase):
    def test_random_state_details(self):
        con = Config()
        self.assertEqual(con.random_seed, 42)
    
    def test_assets_path(self):
        con = Config()
        self.assertEqual(con.assets_path, Path('./assets'))
    
    def test_original_data_file_path(self):
        con = Config()
        self.assertEqual(con.original_data_path, Path('./assets/original_data/dataset.csv'))
    
    def test_train_and_test_datasets_path(self):
        con = Config()
        self.assertEqual(con.dataset_path, Path('./assets/data'))

    def test_train_and_test_features_path(self):
        con = Config()
        self.assertEqual(con.features_path, Path('./assets/features'))
        
    def test_models_file_path(self):
        con = Config()
        self.assertEqual(con.models_path, Path('./assets/models'))
    
    def test_metrics_file_path(self):
        con = Config()
        self.assertEqual(con.metrics_path, Path('./assets/metrics.json'))

