

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(sum(min(A[i], B[i]) for i in range(n)) + min(A[n], B[n-1]))

if __name__ == '__main__':
    main()
