from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from src.utils.utils import save_model
from src.components.model_evaluation import model_evaluater


class Model:
    def __init__(self, train_path, test_path):
        self.train_data_path = train_path
        self.test_data_path = test_path
        self.directory_path = os.path.dirname(self.train_data_path)

    def train(self):
        
        train_data = pd.read_csv(self.train_data_path)

        target_column = train_data.columns[-1]

        Y_train  = train_data[target_column]
        X_train = train_data.drop(target_column, axis = 1)

        

        models = {
                    "Linear Regression": LinearRegression(),
                    "Ridge Regression": Ridge(),
                    "Lasso Regression": Lasso(),
                    "Decision Tree Regressor": DecisionTreeRegressor(),
                    "Random Forest Regressor": RandomForestRegressor(),
                    "Support Vector Regressor": SVR(),
                    "K-Nearest Neighbors Regressor": KNeighborsRegressor()
                 }
        
        self.model_path_dict = {}
        
        for model in models:

            try: 
                logging.info(f"Training {model} model")
                models[model].fit(X_train, Y_train)
                logging.info(f"{model} trained")

                model_path = os.path.join(self.directory_path,f"{model}.pkl")

                logging.info(f"Saving {model} model")
                save_model(models[model], model_path)
                logging.info(f"{model} saved")
                self.model_path_dict[model] = model_path

            except Exception as e:
                raise customexception(e, sys)
            
        return

    def evaluate_model(self):

        try:
            model_eval_obj = model_evaluater()
            model_eval_obj.evaluator(self.model_path_dict, self.test_data_path)

        except Exception as e:
            raise customexception(e, sys)
