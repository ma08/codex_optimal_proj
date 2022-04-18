
import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    count = 0

    for i in range(A, B+1):
        if i % C != 0 and i % D != 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
