KILOBITS_TO_BITS = 1000
KILOBYTES_TO_BITS = 8000

MEGABITS_TO_BITS = 1000000
MEGABYTES_TO_BITS = 8000000

BYTES_TO_BITS = 8

UDP_DEFAULT_BUFFER_SIZE = 8000
UDP_IP_ETHERNET_HEADERS_SIZE = 42

def format_bits_as_measure(bits, measure):
    if measure == 'k':
        return '%.2f Kbits' % (bits / KILOBITS_TO_BITS)
    elif measure == 'K':
        return '%.2f Kbytes' % (bits / KILOBYTES_TO_BITS)
    elif measure == 'm':
        return '%.2f Mbits' % (bits / MEGABITS_TO_BITS)
    elif measure == 'M':
        return '%.2f Mbytes' % (bits / MEGABYTES_TO_BITS)

def format_bits_as_measure_per_second(bits, measure):
    return format_bits_as_measure(bits, measure) + '/sec'
