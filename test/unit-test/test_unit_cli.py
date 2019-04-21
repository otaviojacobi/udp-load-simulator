import sys
sys.path.append('./src')

from unittest import mock
import unittest
import argparse
from cli import CLIParser

class TestCLIParser(unittest.TestCase):

    def test_server_default_args(self):
        cli_namespace = CLIParser().parse(mock_arguments=['-s'])
        default_server_namespace = {
            'server': True,
            'host': None,
            'interval': 1,
            'port': 5201,
            'format': 'm',
            'verbose': False,
            'bandwidth': 1000000,
            'time': 10
        }
        self.assertEqual(default_server_namespace, vars(cli_namespace))

    def test_client_default_args(self):
        cli_namespace = CLIParser().parse(mock_arguments=['-c', 'localhost'])
        default_client_namespace = {
            'server': False,
            'host': 'localhost',
            'interval': 1,
            'port': 5201,
            'format': 'm',
            'verbose': False,
            'bandwidth': 1000000,
            'time': 10
        }
        self.assertEqual(default_client_namespace, vars(cli_namespace))

    def test_server_complete_args(self):
        cli_namespace = CLIParser().parse(mock_arguments=['-s', '-p', '8080', '-i', '3', '--format=K', '-V'])
        complete_server_namespace = {
            'server': True,
            'host': None,
            'interval': 3,
            'port': 8080,
            'format': 'K',
            'verbose': True,
            'bandwidth': 1000000,
            'time': 10
        }
        self.assertEqual(complete_server_namespace, vars(cli_namespace))

    def test_client_complete_args(self):
        cli_namespace = CLIParser().parse(mock_arguments=['-c', '10.127.15.65', '-p', '8080', '-i', '3', '--format=K', '--verbose', '-b', '5K', '--time=20'])
        complete_server_namespace = {
            'server': False,
            'host': '10.127.15.65',
            'interval': 3,
            'port': 8080,
            'format': 'K',
            'verbose': True,
            'bandwidth': 5000,
            'time': 20
        }
        self.assertEqual(complete_server_namespace, vars(cli_namespace))

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='1M'))
    def test_bandwidth_1M(self, mock_args):
        cli_namespace = CLIParser().parse()
        self.assertEqual(cli_namespace.bandwidth, 1000000)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='1K'))
    def test_bandwidth_1K(self, mock_args):
        cli_namespace = CLIParser().parse()
        self.assertEqual(cli_namespace.bandwidth, 1000)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='5M'))
    def test_bandwidth_5M(self, mock_args):
        cli_namespace = CLIParser().parse()
        self.assertEqual(cli_namespace.bandwidth, 5000000)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='6K'))
    def test_bandwidth_6K(self, mock_args):
        cli_namespace = CLIParser().parse()
        self.assertEqual(cli_namespace.bandwidth, 6000)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='999999M'))
    def test_bandwidth_huge_number(self, mock_args):
        cli_namespace = CLIParser().parse()
        self.assertEqual(cli_namespace.bandwidth, 999999000000)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='2.6K'))
    def test_bandwidth_2_6K(self, mock_args):
        with self.assertRaises(SystemExit,):
            cli_namespace = CLIParser().parse()

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='ashuirahs'))
    def test_bandwidth_random_stuff(self, mock_args):
        with self.assertRaises(SystemExit,):
            cli_namespace = CLIParser().parse()

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='ashuirahsM'))
    def test_bandwidth_random_stuff_M(self, mock_args):
        with self.assertRaises(SystemExit,):
            cli_namespace = CLIParser().parse()

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='ashuirahsK'))
    def test_bandwidth_random_stuff_K(self, mock_args):
        with self.assertRaises(SystemExit,):
            cli_namespace = CLIParser().parse()
