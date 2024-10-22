import logging
import os
from datetime import datetime

log_path = os.path.join(os.getcwd(), "logs")
#LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(log_path, exist_ok=True)
#log_path=os.path.join(os.getcwd(),"logs")

timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
#os.makedirs(log_path,exist_ok=True)

LOG_FILE = f"{timestamp}.log"
#LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH, 
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)
