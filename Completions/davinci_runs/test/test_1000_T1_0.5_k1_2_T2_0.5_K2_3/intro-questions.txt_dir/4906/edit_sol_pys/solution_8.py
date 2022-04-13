
import sys

def encode(string):
    # your code here
    pass

def decode(string):
    # your code here
    pass

def main():
    line = sys.stdin.readline().strip()
    if line[0] == "E":
        print(encode(line[2:]))
    else:
        print(decode(line[2:]))

if __name__ == '__main__':
    main()
