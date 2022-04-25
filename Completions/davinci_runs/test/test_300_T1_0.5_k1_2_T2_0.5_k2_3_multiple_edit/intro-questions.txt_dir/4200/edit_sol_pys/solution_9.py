

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    print('Yes' if max(A) < total_votes / (4 * M) else 'No')

if __name__ == '__main__':
    main()
