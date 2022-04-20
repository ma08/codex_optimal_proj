

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    A_max = max(A)
    if A_max < A_sum - A_max:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
