import logging, time

#Dumps an error log to "error.log" file
def create_error_log():
    logging.basicConfig(filename="error.log", format="%(asctime)s - %(message)s")
    logging.exception("Exception occured")
