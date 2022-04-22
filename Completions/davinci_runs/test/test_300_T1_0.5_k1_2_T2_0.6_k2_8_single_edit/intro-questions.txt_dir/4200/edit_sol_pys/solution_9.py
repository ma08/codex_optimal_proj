

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if M == 1:
        if max(A) * 4 <= total_votes:
            print('Yes')
        else:
            print('No')
    else:
        if max(A) * 4 * M <= total_votes:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
