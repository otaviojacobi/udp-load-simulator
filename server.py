from application import Application
import time
import socket
from units import UDP_DEFAULT_BUFFER_SIZE
from threading import Thread, Lock
import units

class Server(Application):

    def __init__(self, port, interval, log_format, verbose):
        super().__init__(port, interval, log_format, verbose)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__bits_received_last_interval = 0
        self.__bits_received_last_second_mutex = Lock()
        self.logging_thread = None

        try:
            self.logger.debug('Trying to bind server to port {}'.format(self.port))
            self.socket.bind(('127.0.0.1', self.port))
            self.logger.debug('Server bound to port {}'.format(self.port))
        except OSError as exception:
            self.logger.critical('Failed to bind socket to port.Port probably already in use.' + str(exception))
            exit(1)

    def handle(self):
        self.logger.info('Started server socket listening on port {}'.format(self.port))
        self.__start_daemon_logging_thread()
        while True:
            self.logger.debug('Waiting for next connection on port {}'.format(self.port))
            data, address = self.socket.recvfrom(UDP_DEFAULT_BUFFER_SIZE)
            self.__bits_received_last_second_mutex.acquire()
            self.__bits_received_last_interval += 8 * len(data)
            self.__bits_received_last_second_mutex.release()

    def __start_daemon_logging_thread(self):
        self.logging_thread = Thread(target=self.__logging_thread)
        self.logging_thread.setDaemon(True)
        self.logging_thread.start()

    def __logging_thread(self):
        while True:
            time.sleep(self.interval)
            self.__bits_received_last_second_mutex.acquire()

            self.logger.debug('Total bits received last interval: {}'.format(self.__bits_received_last_interval))

            bits_per_second_received = self.__bits_received_last_interval / self.interval
            recevied_last_second_with_measure = units.format_bits_as(bits_per_second_received, self.log_format)
            self.logger.info(recevied_last_second_with_measure)

            self.__bits_received_last_interval = 0

            self.__bits_received_last_second_mutex.release()
