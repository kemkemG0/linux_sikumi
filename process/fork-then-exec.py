#!/usr/bin/python3

import os,sys

ret = os.fork()

if ret == 0:
    print(f"child process : pid={os.getpid()}, parent process: ppid={os.getppid()}")
    os.execve("/bin/echo", ["echo", f"hello from pid={os.getpid()}"],{})
    exit()
elif ret>0:
    print(f"parent process : pid={os.getpid()}, child process: ppid={ret}")
    exit()

sys.exit(1)
