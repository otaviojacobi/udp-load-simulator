from .application import Application
from .units import UDP_DEFAULT_BUFFER_SIZE, BYTES_TO_BITS

class Server(Application):

    def __init__(self, port, interval, log_format, verbose):
        super().__init__(port, interval, log_format, verbose)
        try:
            self.logger.debug('Trying to bind server to port {}'.format(self.port))
            self.socket.bind(('127.0.0.1', self.port))
            self.logger.debug('Server bound to port {}'.format(self.port))
        except OSError as exception:
            self.logger.critical('Failed to bind socket to port.Port probably already in use.' + str(exception))
            exit(1)

    def handle(self):
        self.logger.info('Started server socket listening on port {}'.format(self.port))
        self.start_daemon_logging_thread('received')
        while True:
            self.logger.debug('Waiting for next connection on port {}'.format(self.port))
            data, address = self.socket.recvfrom(UDP_DEFAULT_BUFFER_SIZE)
            self.logger.debug('Received {} bytes from host {}'.format(len(data), address))
            # We don't have to worry about cleaning up bits_transfered_last_interval, because the daemon thread handles the reset
            self.increase_transfered_data(BYTES_TO_BITS * len(data))
