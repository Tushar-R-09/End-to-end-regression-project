from src.components.model_trainer import Model
from src.pipeline.feature_pipeline import feature_pipeline
from src.exception.exception import customexception
import sys

class training_pipeline:
    def __init__(self,raw_data_path, target_column = "charges"):
        self.raw_data_path = raw_data_path
        self.target_column = target_column
        self.feature_object = feature_pipeline(self.raw_data_path)

    def start_data_ingestion(self):
        try:
            train_path, test_path = self.feature_object.data_ingestion()
            return train_path, test_path
        except Exception as e:
            raise customexception(e, sys)
        
    def start_data_transformation(self, train_path, test_path):
        try:
            transformed_train_data_path, transformed_test_data_path = self.feature_object.data_transformation(train_path, test_path, self.target_column)
            return transformed_train_data_path, transformed_test_data_path
        except Exception as e:
            raise customexception(e, sys)
        
    def start_model_training(self, transformed_train_path, transformed_test_path):
        try:
            model_object = Model(transformed_train_path, transformed_test_path)
            model_object.train()
            model_object.evaluate_model()
        except Exception as e:
            raise customexception(e, sys)