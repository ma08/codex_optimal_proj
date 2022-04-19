

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    max_votes = max(A)
    if max_votes < total_votes / (4 * M):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
