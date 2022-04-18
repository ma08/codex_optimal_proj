

import sys

def main():
    line = sys.stdin.readline()
    line = line.rstrip("\n")
    for i in range(len(line)-1):
        if line[i] == 's' and line[i+1] == 's':
            print("hiss")
            return
    print("no hiss")

if __name__ == '__main__':
    main()
