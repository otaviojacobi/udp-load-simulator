import argparse
import sys
from units import MEGABITS_TO_BITS, KILOBITS_TO_BITS

class CLIParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.__init_parser_args()

    def __init_parser_args(self):
        self.parser.add_argument('-v', '--version', action='store_true', help='Show version information and quit.')
        client_server_group = self.parser.add_mutually_exclusive_group(required=('--version' not in sys.argv and '-v' not in sys.argv))
        client_server_group.add_argument('-s', '--server', action='store_true', help='Run in server mode. (This will only allow one connection at a time)')
        client_server_group.add_argument('-c', '--client', type=str, dest='host', help='Run in client mode, connecting to an iPerf server running on host.')
        self.parser.add_argument('-i', '--interval', type=int, default=1, help='The interval to which info about measurements shall be displayed. Default to 1.')
        self.parser.add_argument('-p', '--port', type=int, default=5201, help='The server port to the server to listen on and the client to connect to. This should be the same in both client and server. Default is 5201')
        self.parser.add_argument('-f', '--format', choices=['k', 'K', 'm', 'M'], default='m', help='A letter specifying the format to print bandwidth numbers in. Supported formats are "k" = Kbits/sec "K" = KBytes/sec "m" = Mbits/sec "M" = MBytes/sec  The adaptive formats choose between kilo- and mega- as appropriate. Default to m.')
        self.parser.add_argument('-V', '--verbose', action='store_true', help='Give more detailed output')
        self.parser.add_argument('-j', '--json', action='store_true', help='output in JSON format')
        self.parser.add_argument('-b', '--bandwidth', type=str, default='1M', help='[CLIENT ONLY] Set target bandwidth to N[KM] bits/sec. Default 1 Mbit/sec.')
        self.parser.add_argument('-t', '--time', type=int, default=10, help='[CLIENT ONLY] The time in seconds to transmit for. Default is 10 seconds.')

    def __is_valid_bandwidth(self, bandwidth):
        return bandwidth[-1] in ['K', 'M'] and bandwidth[0:-1].isdigit()

    def __convert_bandwidth_to_bits(self, bandwidth):
        measure_unit = bandwidth[-1]
        measure_value = int(bandwidth[0:-1])

        return measure_value * MEGABITS_TO_BITS if measure_unit == 'M' else measure_value * KILOBITS_TO_BITS

    def parse(self, mock_arguments=None):

        args = self.parser.parse_args() if mock_arguments is None else self.parser.parse_args(mock_arguments)

        if args.version:
            print('udp-load-simulator version 1.0.0 (April 2019)')
            exit(1)

        if not self.__is_valid_bandwidth(args.bandwidth):
            self.parser.error('Bandwidth should be in format N[KM] where N is a numeric value')
        args.bandwidth = self.__convert_bandwidth_to_bits(args.bandwidth)
        return args
