from src.pipeline.training_pipeline import training_pipeline


training_object = training_pipeline("insurance.csv")


if __name__ == "__main__":
    train_path, test_path = training_object.start_data_ingestion()
    transformed_train_path, transformed_test_path = training_object.start_data_transformation(train_path, test_path)

    training_object.start_model_training(transformed_train_path, transformed_test_path)