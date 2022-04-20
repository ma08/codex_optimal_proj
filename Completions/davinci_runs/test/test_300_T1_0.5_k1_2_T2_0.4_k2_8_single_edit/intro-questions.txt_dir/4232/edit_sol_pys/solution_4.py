
import sys

def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    n = int(sys.stdin.readline())
    for i in range(n):
        a, b = sys.stdin.readline().strip().split()
        a = int(a)
        b = int(b)
        print(a + b)

if __name__ == "__main__":
    main()
