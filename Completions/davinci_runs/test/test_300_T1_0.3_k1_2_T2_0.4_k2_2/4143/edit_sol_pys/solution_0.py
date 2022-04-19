
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    c = int(sys.stdin.readline().rstrip())
    d = int(sys.stdin.readline().rstrip())
    e = int(sys.stdin.readline().rstrip())
    print(min(n, a, b, c, d, e) + 4)

if __name__ == "__main__":
    main()
