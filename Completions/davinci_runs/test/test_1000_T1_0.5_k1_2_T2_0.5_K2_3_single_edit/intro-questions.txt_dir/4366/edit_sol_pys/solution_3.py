

import sys

def main():
    line = sys.stdin.readline()
    hours, minutes = line.split()
    hours = int(hours)
    minutes = int(minutes)
    print((hours+minutes)%24)

if __name__ == '__main__':
    main()
