from src.cli import CLIParser
from src.client import Client
from src.server import Server

def main():
    args = CLIParser().parse()

    if args.server:
        app = Server(args.port, args.interval, args.format, args.verbose)
    else:
        app = Client(args.port, args.interval, args.format, args.verbose, args.host, args.bandwidth, args.time)

    app.run()

if __name__ == '__main__':
    main()
