
import sys

def main():
    line = sys.stdin.readline()
    A, B = line.split()
    A = int(A)  # convert string to int
    B = int(B)  # convert string to int
    print((A + B) % 24)

if __name__ == '__main__':
    main()
