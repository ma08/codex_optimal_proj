

def main():
    N = int(input())
    A = list(map(int, input().split())
    if N % 2 == 0:
        print(N)
    else:
        if max(A) < total_votes / (4 * M) or min(A) < total_votes / (4 * M):
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()
