

import sys

def main():
    # read lines from stdin
    lines = sys.stdin.readlines()
    # remove newline character from lines
    lines = [line.rstrip("\n") for line in lines]
    # iterate through lines, if s is followed by s, print hiss, otherwise print no hiss
    for line in lines:
        for i in range(len(line)-1):
            if line[i] == 's' and line[i+1] == 's':
                print("hiss")
                break
        else:
            print("no hiss")

if __name__ == '__main__':
    main()
