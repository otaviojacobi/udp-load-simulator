import logging

class Application:

    def __init__(self, port, log_format, verbose):
        self.port = port
        self.log_format = log_format
        self.logger = self.__get_logger(verbose)

    def start(self):
        try:
            self.handle()
        except KeyboardInterrupt:
            self.logger.info('CTRL+c pressed, now Exiting application...See you soon :-)')

    def handle(self):
        raise NotImplementedError('Abstract method <handle> should be implemented by child class.')

    def __get_logger(self, verbose):
        logger = logging.getLogger('application')
        ch = logging.StreamHandler()
        log_level = logging.DEBUG if verbose else logging.INFO
        logger.setLevel(log_level)
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger