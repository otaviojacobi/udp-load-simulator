[![Build Status](https://travis-ci.com/otaviojacobi/udp-load-simulator.png)](https://travis-ci.com/otaviojacobi/udp-load-simulator)

## UDP Load Simulator

This is a tool for simulate load over a network.
It's highly inspired in the Iperf tool.

## How to use it

You can run `python3 main.py -s` to start the server.
You can run `python3 main.py -c localhost` to start the client in the same host machine. You can replace the client HOST for the target machine IP or hostname.

You can also run `python3 main.py -h` to check the full documentation or you can read bellow.
All tests were done in linux, no guaranties to work in macOS/windows systems.

### CLI Arguments
```
usage: main.py [-h] (-s | -c HOST) [-i INTERVAL] [-p PORT] [-f {k,K,m,M}] [-V]
               [-b BANDWIDTH] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -s, --server          Run in server mode. (This will only allow one
                        connection at a time)
  -c HOST, --client HOST
                        Run in client mode, connecting to an iPerf server
                        running on host.
  -i INTERVAL, --interval INTERVAL
                        The interval to which info about measurements shall be
                        displayed. Default to 1.
  -p PORT, --port PORT  The server port to the server to listen on and the
                        client to connect to. This should be the same in both
                        client and server. Default is 5201
  -f {k,K,m,M}, --format {k,K,m,M}
                        A letter specifying the format to print bandwidth
                        numbers in. Supported formats are "k" = Kbits/sec "K"
                        = KBytes/sec "m" = Mbits/sec "M" = MBytes/sec The
                        adaptive formats choose between kilo- and mega- as
                        appropriate. Default to m.
  -V, --verbose         Give more detailed output
  -b BANDWIDTH, --bandwidth BANDWIDTH
                        [CLIENT ONLY] Set target bandwidth to N[KM] bits/sec.
                        Default 1 Mbit/sec.
  -t TIME, --time TIME  [CLIENT ONLY] The time in seconds to transmit for.
                        Default is 10 seconds.
```
