import sys
def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
