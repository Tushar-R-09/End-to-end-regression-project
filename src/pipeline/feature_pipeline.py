from src.components.data_ingestion import Data_Ingestion
from src.components.data_transformation import data_preprocessor




class feature_pipeline:
    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path

    def start_pipeline(self):

        data_ingestion_obj = Data_Ingestion(self.raw_data_path)

        train_path, test_path = data_ingestion_obj.initiate_data_ingestion()


        preprocessor_object = data_preprocessor()

        transformed_train_data_path, transformed_test_data_path = preprocessor_object.initiate_preprocessing(train_path, test_path, 'charges')

        return transformed_train_data_path, transformed_test_data_path