from src.pipeline.feature_pipeline import feature_pipeline


obj = feature_pipeline("insurance.csv")

if __name__ == "__main__":
    obj.start_pipeline()