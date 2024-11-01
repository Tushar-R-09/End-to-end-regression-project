from src.components.model_trainer import Model

class training_pipeline:
    def __init__(self, train_data_path, test_data_path):
        self.trainer = Model(train_data_path, test_data_path)

    def start_pipeline(self):
        
        self.trainer.train()

        self.trainer.evaluate_model()

        return 