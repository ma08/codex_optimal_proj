import sys

def main():
    n = int(sys.stdin.readline())
    print(int(bin(n)[:1:-1], 2))  # print the reversed binary representation of the number

if __name__ == "__main__":
    main()
