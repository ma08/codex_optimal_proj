

import sys

def main():
    # read lines from stdin
    lines = sys.stdin.readlines()
    # iterate through lines
    for line in lines:
        # remove newline character from line
        line = line.rstrip("\n")
        # iterate through line, if s is followed by s, print hiss, otherwise print no hiss.
        for i in range(len(line)-1):
            if line[i] == 's' and line[i+1] == 's':
                print("hiss")
                break
        else:
            print("no hiss")

if __name__ == '__main__':
    main()
