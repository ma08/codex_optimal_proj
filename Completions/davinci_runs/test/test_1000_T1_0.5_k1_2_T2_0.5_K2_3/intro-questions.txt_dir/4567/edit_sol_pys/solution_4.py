
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(i) for i in sys.stdin.readline().rstrip().split()]
    A.sort()
    if A[-1] >= 10:
        print(A[-1])
    elif A[-1] + A[-2] >= 10:
        print(A[-1] + A[-2])
    else:
        print(A[-1] + A[-2] + A[-3])

if __name__ == '__main__':
    main()
