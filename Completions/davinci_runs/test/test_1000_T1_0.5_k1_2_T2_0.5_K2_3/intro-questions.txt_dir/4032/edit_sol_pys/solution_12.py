

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))[:n]
    print(A[k-1])

if __name__ == '__main__':
    main()
