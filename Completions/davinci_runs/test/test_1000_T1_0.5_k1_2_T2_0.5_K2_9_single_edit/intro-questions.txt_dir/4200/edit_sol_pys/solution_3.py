

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if max(A) >= total_votes / (4 * M):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
