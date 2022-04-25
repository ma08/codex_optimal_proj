#!/usr/bin/python

import os

def main():
    print "Checking if file exists"
    if os.path.isfile('/home/pi/Desktop/data/log.txt'):
        print "File exists"
    else:
        print "File does not exist"

if __name__ == '__main__':
    main()
