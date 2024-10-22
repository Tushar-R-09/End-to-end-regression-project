from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from src.utils.utils import save_preprocessor
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

class data_preprocessor:
    def __init__(self):
        return 
    
    def preprocessor(self, data):
        try:
            category_columns = data.select_dtypes(include=["object"]).columns.values
            numeric_columns = data.select_dtypes(exclude=["object"]).columns.values

            num_pipeline = Pipeline([
                                        ('imputer', SimpleImputer(strategy='median')), 
                                        ('scaler', StandardScaler())  # Standardize features
                                    ])
            
            cat_pipeline = Pipeline([
                                        ("imputer", SimpleImputer(strategy='most_frequent')),
                                        ("onehot", OneHotEncoder(handle_unknown='ignore'))  # handle_unknown='ignore' to avoid errors on unseen categories
                                    ])
            
            # Combine pipelines using ColumnTransformer
            preprocessor = ColumnTransformer([
                ('cat', cat_pipeline, category_columns),
                ('num', num_pipeline, numeric_columns)
            ])

            return preprocessor
        
        except Exception as e:
            logging.info("Exception raised when creating a preprocessor")
            raise customexception(e,sys)
        
    def initiate_preprocessing(self, train_data_path, test_data_path, target_column):

        try:
            train_data = pd.read_csv(train_data_path)
            logging.info("train data read")

            test_data = pd.read_csv(test_data_path)
            logging.info("test data read")

            train_data_input_features = train_data.drop(target_column, axis = 1)
            train_data_target_feature = train_data[target_column]

            test_data_input_features = test_data.drop(target_column, axis = 1)
            test_data_target_feature = test_data[target_column]

            preprocessor = self.preprocessor(train_data_input_features)

            logging.info("Data preprocessing created")

            transformed_train_data_features = preprocessor.fit_transform(train_data_input_features)

            transformed_test_data_features = preprocessor.transform(test_data_input_features)

            train_array = np.c_[transformed_train_data_features, np.array(train_data_target_feature)]

            test_array = np.c_[transformed_test_data_features, np.array(test_data_target_feature)]

            no_of_columns = train_array.shape[1]

            no_of_features = no_of_columns - 1

            feature_columns = []

            x = 'feature'
            for i in range(1, no_of_features + 1):
                feature_columns.append(x+f'_{str(i)}')

            feature_columns.append('target')


            train_df = pd.DataFrame(train_array, columns=feature_columns)

            test_df = pd.DataFrame(test_array, columns=feature_columns)

            directory_path = os.path.dirname(train_data_path)

            train_csv_path = os.path.join(directory_path, 'transformed_train_file.csv')

            test_csv_path =  os.path.join(directory_path, 'transformed_test_file.csv')

            train_df.to_csv(train_csv_path, index=False)

            test_df.to_csv(test_csv_path, index=False)

            save_preprocessor(preprocessor, "artifacts/preprocessor.pkl")


            return train_csv_path, test_csv_path
        
        except Exception as e:
            raise customexception(e,sys)