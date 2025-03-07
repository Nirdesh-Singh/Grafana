import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

messages_info = ["Service started", "Processing request", "Database connection successful", "User login successful"]
messages_error = ["Database connection failed", "Service crashed", "Request timeout", "Invalid user input"]

while True:
    if random.random() < 0.8:
        logging.info(random.choice(messages_info))
    else:
        logging.error(random.choice(messages_error))
    time.sleep(random.uniform(1, 3))  # Sleep between 1-3 seconds
