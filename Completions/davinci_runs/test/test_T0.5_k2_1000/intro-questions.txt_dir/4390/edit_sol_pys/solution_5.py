import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(b - a % b) 

if __name__ == "__main__":
    main()
