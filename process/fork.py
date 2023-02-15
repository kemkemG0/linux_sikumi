#!/usr/bin/python3

import os, sys

print('aaaa')

ret = os.fork()

print('bbb')


if ret == 0:
    # when child process
    print(f"child:pid={os.getpid()}, parent:ppid={os.getppid()}")
elif ret > 0:
    print(f"parent:ppid={os.getpid()}, child:pid={ret}")