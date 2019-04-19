from application import Application
import socket
import time

class Client(Application):

    def __init__(self, port, log_format, verbose, server_host, bandwidth, time):
        super().__init__(port, log_format, verbose)
        self.server_host = server_host
        self.bandwidth = bandwidth
        self.time = time
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def handle(self):
        self.logger.info('Started client socket to connect to server on port {}'.format(self.port))
        while True:
            self.socket.sendto(bytearray(1024), (self.server_host, self.port))
            time.sleep(1)
