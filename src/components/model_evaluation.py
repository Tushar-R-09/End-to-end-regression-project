from src.logger.logging import logging
from src.exception.exception import customexception
import mlflow
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.utils.utils import load_model
from src.utils.utils import save_model
import os
import pandas as pd
class model_evaluater:

    def __init__(self):
        return
    
    def evaluator(self, model_path_dict, test_data_path):
        
        try:
            test_data = pd.read_csv(test_data_path)
            target_column = test_data.columns[-1]

            Y_test = test_data[target_column]
            X_test = test_data.drop(target_column, axis = 1)
            best_r2 = -999999
            for model in model_path_dict:
                model_path = model_path_dict[model]
                model = load_model(model_path)

                y_pred = model.predict(X_test)

                mse = mean_squared_error(Y_test, y_pred)
                mae = mean_absolute_error(Y_test, y_pred)
                r2 = r2_score(Y_test, y_pred)

                if r2 > best_r2:
                    best_r2 = r2
                    best_model = model
                    best_model_path = model_path

                with mlflow.start_run():
                    mlflow.log_param("model", model)
                    mlflow.log_metric("MSE", mse)
                    mlflow.log_metric("MAE", mae)
                    mlflow.log_metric("R2_Score", r2)

            # with mlflow.start_run():
            #     mlflow.sklearn.log_model(model, "model", registered_model_name="best_model")

            directory_path = os.path.dirname(best_model_path)
            best_model_path = os.path.join(directory_path,'best_model.pkl')
            save_model(best_model, best_model_path)

        except Exception as e:
            raise customexception(e, sys)
