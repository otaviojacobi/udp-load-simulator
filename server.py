from application import Application

class Server(Application):

    def __init__(self, port, log_format, verbose, is_daemon, pidfile):
        super().__init__(port, log_format, verbose)
        self.is_daemon = is_daemon
        self.pidfile = pidfile
    
    def start(self):
        print('Starting...')