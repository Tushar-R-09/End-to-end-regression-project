from src.components.data_ingestion import Data_Ingestion
from src.components.data_transformation import data_preprocessor
from src.exception.exception import customexception
import sys




class feature_pipeline:
    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path

    def data_ingestion(self):

        try:
            data_ingestion_obj = Data_Ingestion(self.raw_data_path)

            train_path, test_path = data_ingestion_obj.initiate_data_ingestion()

            return train_path, test_path
        except Exception as e:
            raise customexception(e, sys)
    
    def data_transformation(self, train_path, test_path, target_column = "charges"):

        try: 
            data_transformation_obj = data_preprocessor()

            transformed_train_data_path, transformed_test_data_path = data_transformation_obj.initiate_preprocessing(train_path, test_path, target_column)

            return transformed_train_data_path, transformed_test_data_path
        except Exception as e:
            raise customexception(e, sys)

    def start_pipeline(self):

        try: 
            train_path, test_path = self.data_ingestion()
            transformed_train_data_path, transformed_test_data_path = self.data_transformation(train_path, test_path)
            return transformed_train_data_path, transformed_test_data_path
        
        except Exception as e:
            raise customexception(e, sys)

        

       