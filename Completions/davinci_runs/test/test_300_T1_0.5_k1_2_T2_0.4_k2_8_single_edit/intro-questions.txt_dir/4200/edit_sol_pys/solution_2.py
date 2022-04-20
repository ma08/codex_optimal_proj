

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if max(A) < total_votes / (4 * M):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
