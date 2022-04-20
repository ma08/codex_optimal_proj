
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        a, b = sys.stdin.readline().strip().split()
        a = int(a)
        b = int(b)
        print(a + b)

if __name__ == "__main__":
    main()
