

def main():
    N = int(input())
    A = list(map(int, input().split()))[:N]
    if all(v == 0 for v in A):
        print(0)
    else:
        if max(A) < total_votes / (4 * M):
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()
