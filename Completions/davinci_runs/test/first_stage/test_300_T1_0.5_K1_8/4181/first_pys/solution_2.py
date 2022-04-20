

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    total = 0
    for i in range(n):
        total += min(A[i] + A[i+1], B[i])
    print(total)

if __name__ == '__main__':
    main()