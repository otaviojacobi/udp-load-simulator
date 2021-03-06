import time
from application import Application
from units import UDP_DEFAULT_BUFFER_SIZE, BYTES_TO_BITS, UDP_IP_ETHERNET_HEADERS_SIZE


class Client(Application):

    def __init__(self, port, interval, log_format, verbose, server_host, bandwidth, time, is_json):
        super().__init__(port, interval, log_format, verbose, is_json)

        if server_host == 'localhost' or server_host == '127.0.0.1':
            self.server_host = self.get_ip_address()
        else:
            self.server_host = server_host

        self.bandwidth = bandwidth
        self.time = time

        bandwidth_in_bytes = self.bandwidth // BYTES_TO_BITS
        full_buffer_iterations = bandwidth_in_bytes // UDP_DEFAULT_BUFFER_SIZE
        last_buffer_iteration = (bandwidth_in_bytes / UDP_DEFAULT_BUFFER_SIZE) - full_buffer_iterations
        last_buffer_iteration_size = int(last_buffer_iteration * UDP_DEFAULT_BUFFER_SIZE)

        self.full_buffer_iterations = full_buffer_iterations
        self.last_buffer_iteration_size = last_buffer_iteration_size
        self.UDP_PACKAGE = bytearray(UDP_DEFAULT_BUFFER_SIZE - UDP_IP_ETHERNET_HEADERS_SIZE)
        self.CORRECTION_PACKAGE = bytearray(self.last_buffer_iteration_size - UDP_IP_ETHERNET_HEADERS_SIZE)
        self.SLEEP_TIME = float(1/(self.full_buffer_iterations + 1))
        self.server_address = (self.server_host, self.port)

        self.logger.debug('Bandwidth in BYTES {}'.format(bandwidth_in_bytes))
        self.logger.debug('Amount of iterations {}'.format(full_buffer_iterations))
        self.logger.debug('Last Iteration Size {} BYTES'.format(last_buffer_iteration_size))

    def handle(self):
        self.logger.info('Started client socket to send load to server {}'.format((self.server_host, self.port)))
        self.start_daemon_logging_thread('sent')
        for _ in range(self.time):
            self.__send_bits()

    def __send_bits(self):
        for _ in range(self.full_buffer_iterations):
            self.socket.sendto(self.UDP_PACKAGE, self.server_address)
            # We don't have to worry about cleaning up bits_transfered_last_interval, because the daemon thread handles the reset
            self.increase_transfered_data(BYTES_TO_BITS * UDP_DEFAULT_BUFFER_SIZE)
            time.sleep(self.SLEEP_TIME)

        if self.last_buffer_iteration_size != 0:
            self.socket.sendto(self.CORRECTION_PACKAGE, self.server_address)
            # We don't have to worry about cleaning up bits_transfered_last_interval, because the daemon thread handles the reset
            self.increase_transfered_data(BYTES_TO_BITS * self.last_buffer_iteration_size)
            time.sleep(self.SLEEP_TIME)
