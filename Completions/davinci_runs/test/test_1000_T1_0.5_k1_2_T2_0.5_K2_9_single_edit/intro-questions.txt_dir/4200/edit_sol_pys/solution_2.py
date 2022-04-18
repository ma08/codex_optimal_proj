
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total_votes = sum(A)
    if M == 1:
        if max(A) < total_votes / 4:
            print('No')
        else:
            print('Yes')
    else:
        if max(A) < total_votes / (4 * M):
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()
