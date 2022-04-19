

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))[:N]
    total_votes = sum(A[:N])
    if max(A) < total_votes / (4 * M):
        print('No')
    else: print('Yes')

if __name__ == '__main__':
    main()
