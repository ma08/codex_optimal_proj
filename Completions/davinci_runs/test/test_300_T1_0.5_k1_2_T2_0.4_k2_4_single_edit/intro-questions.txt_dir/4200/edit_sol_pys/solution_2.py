

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total_votes = sum(A) / (4 * M)
    if A[M - 1] >= total_votes:
        print('Yes')
    print('No')

if __name__ == '__main__':
    main()
