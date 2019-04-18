from cli import CLIParser
from client import Client
from server import Server

def main():
    args = CLIParser().parse()

    if args.server:
        app = Server(args.port, args.format, args.verbose)
    else:
        app = Client(args.port, args.format, args.verbose, args.bandwidth, args.time)

    app.start()

if __name__ == '__main__':
    main()