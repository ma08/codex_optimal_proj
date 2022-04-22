

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if M == 1:
        if max(A) < total_votes / 4.0:
            print('No')
        else:
            print('Yes')
    else:
        if max(A) < total_votes / (4.0 * M):
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()
