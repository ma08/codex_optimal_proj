
import sys

def main():
    N = int(sys.stdin.readline().strip())
    A = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    B = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print(A, B)

if __name__ == '__main__':
    main()
