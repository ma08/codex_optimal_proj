#!/usr/bin/env python3
'''
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    a single joystick
'''

import sys

def main():
    m = int(sys.stdin.readline().strip())
    x = 1
    while x <= m:
        if len(set([a**3 + b**3 for a in range(1, x) for b in range(1, x)])) >= x:
            return x
        x += 1
    return 'none'

print(main())
