
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        assert n == len(a)
        print(max(a))
 
if __name__ == '__main__':
    main()
