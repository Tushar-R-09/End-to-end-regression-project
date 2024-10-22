import os

def create_structure_from_paths(file_paths):
    directories = set()
    
    # First, collect all unique directories
    for file_path in file_paths:
        # Check if the path is a directory or a file
        if os.path.splitext(file_path)[1] == '':
            # It is a directory
            directories.add(file_path)
        else:
            # It is a file
            directory = os.path.dirname(file_path)
            if directory:
                directories.add(directory)
    
    # Create all directories
    for directory in directories:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
    
    # Create all files
    for file_path in file_paths:
        if os.path.splitext(file_path)[1] != '':
            # It is a file
            if not os.path.isfile(file_path):
                with open(file_path, 'w') as file:
                    file.write('')  # Write an empty content or add some default content
                print(f"Created file: {file_path}")

# Example usage
file_paths = [
    'experiment/experiment.ipynb',
    'logs',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_evaluation.py',
    'src/components/model_trainer.py',
    'src/exception/__init__.py',
    'src/exception/exception.py',
    'src/logger/__init__.py',
    'src/logger/logging.py',
    'src/pipeline/__init__.py',
    'src/pipeline/feature_pipeline.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/inference_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/__init__.py',
    'templates',
    'tests/integration/__init__.py',
    'tests/unit/__init__.py',
    'app.py',
    'init_setup.sh',
    'requirements.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'test.py'
]

create_structure_from_paths(file_paths)
