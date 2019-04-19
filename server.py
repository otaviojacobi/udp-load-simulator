from application import Application
import time
import socket

class Server(Application):

    def __init__(self, port, log_format, verbose):
        super().__init__(port, log_format, verbose)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.logger.debug('Trying to bind server to port {}'.format(self.port))
            self.socket.bind(('127.0.0.1', self.port))
            self.logger.debug('Server bound to port {}'.format(self.port))
        except OSError as exception:
            self.logger.critical('Failed to bind socket to port.Port probably already in use.' + str(exception))
            exit(1)

    def handle(self):
        self.logger.info('Started server socket listening on port {}'.format(self.port))
        while True:
            self.logger.debug('Waiting for next connection on port {}'.format(self.port))
            data, address = self.socket.recvfrom(1024)
            self.logger.debug('Recevied data, size:{}, from: {}'.format(len(data), address))
