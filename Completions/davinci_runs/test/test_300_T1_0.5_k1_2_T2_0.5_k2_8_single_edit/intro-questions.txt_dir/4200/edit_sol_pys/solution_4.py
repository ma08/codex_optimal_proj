

def main():
    N, M = map(float, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A) / M
    print('Yes' if max(A) >= total_votes else 'No')

if __name__ == '__main__':
    main()
