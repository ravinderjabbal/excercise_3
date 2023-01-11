import logging
import time


class Logger:

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # Setting the format
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        # setting the time format
        curr_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        # Creating and saving the log file
        self.LogFileName = '..//Logs//log_' + curr_time + '.txt'
        # "a" to append the logs in same file
        fh = logging.FileHandler(self.LogFileName, mode="a")
        # formatter set
        fh.setFormatter(fmt)
        # log level set (default info)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
    #
    # def adb_logging(self):
    #     pass
