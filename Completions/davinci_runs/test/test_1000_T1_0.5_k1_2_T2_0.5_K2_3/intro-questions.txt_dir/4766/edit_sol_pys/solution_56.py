#

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        command = sys.stdin.readline()
        if command[:11] == "Simon says":
            print(command[12:])

main()
