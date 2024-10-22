from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Data_Ingestion:
    def __init__(self, data_path):
        self.data_path = data_path
        logging.info("Data path stored")
        return

    def initiate_data_ingestion(self, test_ration = 0.2):
        data = pd.read_csv(self.data_path)
        logging.info("PDF read")

        train_set, test_set = train_test_split(data, test_size=test_ration, random_state=42)
        logging.info("Data split into train and test set")

        os.makedirs('artifacts', exist_ok=True)
        logging.info("artifacts folder made")


        train_csv_path = 'artifacts/train_file.csv'
        test_csv_path = 'artifacts/test_file.csv'

        train_set.to_csv(train_csv_path, index=False)
        test_set.to_csv(test_csv_path, index=False)
        logging.info("Train data and test data is saved")

        return train_csv_path, test_csv_path