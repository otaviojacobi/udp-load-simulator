from application import Application
import daemon
import lockfile
import time

class Server(Application):

    def __init__(self, port, log_format, verbose):
        super().__init__(port, log_format, verbose)
    
    def start(self):
        while True:
            time.sleep(1)
            print('oi')