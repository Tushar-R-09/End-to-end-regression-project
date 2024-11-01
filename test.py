from src.pipeline.feature_pipeline import feature_pipeline
from src.pipeline.training_pipeline import training_pipeline


feature_object = feature_pipeline("insurance.csv")


if __name__ == "__main__":
    transformed_train_data_path, transformed_test_data_path = feature_object.start_pipeline()
    training_object = training_pipeline(transformed_train_data_path, transformed_test_data_path)
    training_object.start_pipeline()