

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A) * (4 * M)
    if max(A) >= total_votes / 4:
        print('Yes')
    print('No')

if __name__ == '__main__':
    main()
