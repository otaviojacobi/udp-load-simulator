import sys
sys.path.append('./src')
import unittest
from units import format_bits_as_measure, format_bits_as_measure_per_second

class TestUnits(unittest.TestCase):

    def test_format_bits_as_measure_1k(self):
        measure = format_bits_as_measure(1000, 'k')
        self.assertEqual(measure, '1.00 Kbits')

    def test_format_bits_as_measure_1m(self):
        measure = format_bits_as_measure(1000000, 'm')
        self.assertEqual(measure, '1.00 Mbits')

    def test_format_bits_as_measure_1K(self):
        measure = format_bits_as_measure(8000, 'K')
        self.assertEqual(measure, '1.00 Kbytes')

    def test_format_bits_as_measure_1M(self):
        measure = format_bits_as_measure(8000000, 'M')
        self.assertEqual(measure, '1.00 Mbytes')

    def test_format_bits_as_measure_1kps(self):
        measure = format_bits_as_measure_per_second(1000, 'k')
        self.assertEqual(measure, '1.00 Kbits/sec')

    def test_format_bits_as_measure_1mps(self):
        measure = format_bits_as_measure_per_second(1000000, 'm')
        self.assertEqual(measure, '1.00 Mbits/sec')

    def test_format_bits_as_measure_1Kps(self):
        measure = format_bits_as_measure_per_second(8000, 'K')
        self.assertEqual(measure, '1.00 Kbytes/sec')

    def test_format_bits_as_measure_1Mps(self):
        measure = format_bits_as_measure_per_second(8000000, 'M')
        self.assertEqual(measure, '1.00 Mbytes/sec')
