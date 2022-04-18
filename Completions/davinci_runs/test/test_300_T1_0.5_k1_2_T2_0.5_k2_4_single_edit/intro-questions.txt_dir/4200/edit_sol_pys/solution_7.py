
def main():
    N, M = map(int, input().split())
    A = map(int, input().split())
    total_votes = sum(A) / (4 * M)
    print('Yes' if max(A) >= total_votes else 'No')

if __name__ == '__main__':
    main()
