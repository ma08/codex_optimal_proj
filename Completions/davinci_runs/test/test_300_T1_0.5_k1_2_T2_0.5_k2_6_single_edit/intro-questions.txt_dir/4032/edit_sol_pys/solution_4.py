

def main():
    n, k, z = map(int, input().split())
    A = list(map(int, input().split()))
    ans = A[0] + A[1]
    for i in range(z+1):
        tmp = 0
        for j in range(i+1):
            tmp += A[j]
            if j < i:
                tmp += A[j+1]
        ans = max(ans, tmp)
    print(ans, end='')

if __name__ == '__main__':
    main()
