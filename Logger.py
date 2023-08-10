import os
from datetime import date
import logging

class Logger():
    """
    Logger to save logs of temperature
    """

    def __init__(self, logs_dir):   # file_name
        today_date = date.today()   # get the current date
        formatted_date = today_date.strftime("%d_%m_%Y")    # convert the date to a specific format

        logger_fn = 'logger_{}.txt'.format(formatted_date)
        logger_path = os.path.join(logs_dir, logger_fn)

        self.logger = logging.getLogger(__name__)   # give a name to logger
        self.logger.setLevel(logging.INFO)  # set the level of logger

        formatter_temp = logging.Formatter(  # define the log format for temp
            'At %(asctime)s current CPU temp is: %(message)s'
        )

        formatter_traceback = logging.Formatter(  # define the log format for traceback
            'At %(asctime)s - %(levelname)s traceback was caught:\n%(message)s'
        )

        # create the file handler for temp stream
        file_handler1 = logging.FileHandler(logger_path)
        file_handler1.setLevel(logging.INFO)
        file_handler1.setFormatter(formatter_temp)
        
        # create the file handler for traceback stream
        file_handler2 = logging.FileHandler(logger_path)
        file_handler2.setLevel(logging.ERROR)
        file_handler2.setFormatter(formatter_traceback)

        self.logger.addHandler(file_handler1)
        self.logger.addHandler(file_handler2)

    def info(self, msg):
        """
        Pass the message to formatter
        """
        self.logger.info(str(msg))

    def error_traceback(self, err):
        """
        Pass the traceback to formatter
        """
        self.logger.error(err)

    def close(self):
        """
        Close the logging process
        """
        logging.shutdown()
