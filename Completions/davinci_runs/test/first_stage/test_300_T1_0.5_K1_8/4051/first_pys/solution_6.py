

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # If the array is already sorted, it can be sorted correctly.
    if sorted(a) == a:
        print('YES')
        return

    # If there is a number that is 2 or more greater than the number before it,
    # the algorithm will not sort correctly.
    for i in range(1, n):
        if a[i] >= a[i-1] + 2:
            print('NO')
            return

    print('YES')

if __name__ == '__main__':
    main()