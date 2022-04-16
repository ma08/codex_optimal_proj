
import sys

def main():
    n = int(sys.stdin.readline())
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    if n == 1:
        print(0)
    elif n == 2:
        print(min(a, b))
    else:
        if a < c:
            print(a + min(b, c * (n - 2)))
        else:
            print(min(c * (n - 1), a + b))
if __name__ == "__main__":
    main()
