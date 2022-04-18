
import sys

def main():
    # read line from stdin
    line = sys.stdin.readline()
    # remove newline character from line
    line = line.rstrip("\n")
    # iterate through line, if s is followed by s, print hiss
    for i in range(len(line)-1):
        if line[i] == 's' and line[i+1] == 's':
            print("hiss")
            return
    # otherwise print no hiss
    else:
        print("no hiss")

if __name__ == '__main__':
    main()
