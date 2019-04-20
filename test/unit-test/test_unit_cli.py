import sys
sys.path.append('./src')

from unittest import mock
import argparse
from cli import CLIParser

@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(bandwidth='1M'))
def test_answer(mock_args):
    cli_namespace = CLIParser().parse()
    assert cli_namespace.bandwidth == 1000000, "Check if bandwidth is properly converted"
