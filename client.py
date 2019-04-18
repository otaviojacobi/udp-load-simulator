from application import Application

class Client(Application):

    def __init__(self, port, log_format, verbose, bandwidth, time):
        super().__init__(port, log_format, verbose)
        self.bandwidth = bandwidth
        self.time = time

    def start(self):
        print('Starting...')