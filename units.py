KILOBITS_TO_BITS = 1000
KILOBYTES_TO_BITS = 8000

MEGABITS_TO_BITS = 1000000
MEGABYTES_TO_BITS = 8000000

UDP_DEFAULT_BUFFER_SIZE = 8000

def format_bits_as(bits, measure):
    if measure == 'k':
        return '%.2f Kbits/sec' % (bits / KILOBITS_TO_BITS)
    elif measure == 'K':
        return '%.2f Kbytes/sec' % (bits / KILOBYTES_TO_BITS)
    elif measure == 'm':
        return '%.2f Mbits/sec' % (bits / MEGABITS_TO_BITS)
    elif measure == 'M':
        return '%.2f Mbytes/sec' % (bits / MEGABYTES_TO_BITS)
