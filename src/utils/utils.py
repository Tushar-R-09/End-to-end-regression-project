import pickle


def save_model(model, model_filepath):
    # Save the model to a file
    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)

    return

def load_model(model_path):

    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model

def save_preprocessor(preprocessor_object, preprocessor_path):

    with open(preprocessor_path, 'wb') as file:
        pickle.dump(preprocessor_object, file)

    return

def load_preprocessor(preprocessor_path):

    with open(preprocessor_path, 'rb') as file:
        loaded_preprocessor = pickle.load(file)

    return loaded_preprocessor
