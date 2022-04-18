
import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    print(socks)

if __name__ == "__main__":
    main()
