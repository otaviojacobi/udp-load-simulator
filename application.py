import logging
from threading import Thread, Lock
import time
import units
import socket

class Application:

    def __init__(self, port, interval, log_format, verbose):
        self.port = port
        self.interval = interval
        self.log_format = log_format
        self.logger = self.__get_logger(verbose)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.__bits_transfered_last_interval = 0
        self.__bits_transfered_last_second_mutex = Lock()
        self.__logging_thread = None

    def run(self):
        '''
        run is the main function to run the application.
        run will call the handle method and handle OS interruptions.
        '''
        try:
            self.handle()
        except KeyboardInterrupt:
            self.logger.info('CTRL+c pressed, now Exiting application...See you soon :-)')

    def handle(self):
        '''
        handle is main method to be implemented by each class.
        handle should always be implemented by child class.
        '''
        raise NotImplementedError('Abstract method <handle> should be implemented by child class.')

    def start_daemon_logging_thread(self, mode):
        '''
        start_daemon_logging_thread starts a daemon thread which logs the amount of data transfered each interval.
        mode - The transfered mode as string: Usually just "sent" ou "received"
        '''
        self.logger.debug('Creating daemon thread with parameter {}'.format(mode))
        self.__logging_thread = Thread(target=self.__run_logging_thread, args=(mode,))
        self.__logging_thread.setDaemon(True)
        self.__logging_thread.start()

    def increase_transfered_data(self, incr_by):
        '''
        increase_transfered_data thread safely increases the amount of transfered data by incr_by
        incr_by - The value to increase the amount of data transfered
        '''
        self.__bits_transfered_last_second_mutex.acquire()
        try:
            self.__bits_transfered_last_interval += incr_by
        except Exception as e:
            self.logger.critical('Error when handling __bits_transfered_last_interval increase. ' + str(e))
        finally:
            self.__bits_transfered_last_second_mutex.release()

    def __run_logging_thread(self, mode):
        self.logger.debug('Logging thread called with parameter {}'.format(mode))
        while True:
            time.sleep(self.interval)
            self.__bits_transfered_last_second_mutex.acquire()

            self.logger.debug('Total bits {} last interval: {}'.format(mode, self.__bits_transfered_last_interval))

            total_transfered_with_unit = units.format_bits_as_measure(self.__bits_transfered_last_interval, self.log_format)

            bits_per_second_transfered = self.__bits_transfered_last_interval / self.interval
            transfered_per_second_with_unit = units.format_bits_as_measure_per_second(bits_per_second_transfered, self.log_format)

            self.logger.info('| {} | Transfered {} | Bandwitch {}'.format(mode, total_transfered_with_unit, transfered_per_second_with_unit))

            # This is ugly. Logging thread ALSO resets for the next printing iteration.
            self.__bits_transfered_last_interval = 0

            self.__bits_transfered_last_second_mutex.release()

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
