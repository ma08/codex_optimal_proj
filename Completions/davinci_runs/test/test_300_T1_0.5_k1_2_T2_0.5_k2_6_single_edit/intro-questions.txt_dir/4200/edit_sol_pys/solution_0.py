

def main():
    N, M = map(int, input().split())
    A = list(map(lambda x: int(x) * (-1), input().split()))
    total_votes = sum(A)
    if M == 1 and total_votes / 4 < max(A):
        print('No')
    elif M != 1 and total_votes / (4 * M) < max(A):
        print('No')
    print('Yes')

if __name__ == '__main__':
    main()
