


def solve(n, sequence):  # O(n)
    if n == 1:  # O(1)
        return 0  # O(1)
    elif n == 2:  # O(1)
        return 0  # O(1)
    else:  # O(1)
        diff = sequence[1] - sequence[0]  # O(1)
        i = 2  # O(1)
        while i < n:  # O(n)
            if sequence[i] - sequence[i-1] != diff:  # O(1)
                return -1  # O(1)
            i += 1  # O(1)
        return 0  # O(1)


if __name__ == '__main__':
    n = int(input())  # O(1)
    sequence = [int(x) for x in input().split()]  # O(n)
    print(solve(n, sequence))  # O(1)
