

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N//2] - A[N//2-1])


if __name__ == '__main__':
    main()
