import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        print(0)
    else:
        for i in range(1, 100):
            if int(i * 0.08) == A and int(i * 0.1) == B:
                print(i)
                return
        print(-1)

if __name__ == '__main__':
    main()
