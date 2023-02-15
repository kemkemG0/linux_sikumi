#!/usr/bin/python3

def test():
    print(signal.SIGINT)


import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
    pass
