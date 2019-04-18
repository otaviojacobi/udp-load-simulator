from application import Application
import socket

class Client(Application):

    def __init__(self, port, log_format, verbose, server_host, bandwidth, time):
        super().__init__(port, log_format, verbose)
        self.server_host = server_host
        self.bandwidth = bandwidth
        self.time = time
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        self.logger.info('Started client socket to connect to server on port {}'.format(self.port))
        try:
            while True:
                self.__handle_client()
        except KeyboardInterrupt:
            self.logger.info('CTRL+c pressed, now Exiting application...See you soon :-)')
    
    def __handle_client(self):
        msg = input('Message to send to server: \n')
        self.socket.sendto(msg.encode(), (self.server_host, self.port))