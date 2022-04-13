
import sys

def main():
    a, b, c = [int(x) for x in sys.stdin.readline().split()]
    print(a * b * c)

if __name__ == "__main__":
    main()
