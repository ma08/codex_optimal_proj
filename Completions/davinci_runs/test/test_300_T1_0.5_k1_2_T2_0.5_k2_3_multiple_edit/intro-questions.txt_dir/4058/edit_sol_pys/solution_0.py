
def get_input(f):
    n, r = [int(x) for x in f.readline().split()]
    a = [int(x) for x in f.readline().split()]
    return n, r, a[:n]

    """
    >>> solve(5, 2, [1, 0, 0, 0, 1]) == 2
    True
    >>> solve(5, 2, [1, 0, 0, 0, 0]) == -1
    True
    >>> solve(5, 2, [1, 1, 0, 0, 0]) == -1
    True
    >>> solve(5, 2, [0, 0, 0, 0, 0]) == -1
    True
    >>> solve(5, 2, [0, 0, 0, 0, 1]) == 1
    True
    >>> solve(5, 2, [1, 0, 1, 0, 1]) == 0
    True
    >>> solve(5, 2, [1, 0, 1, 0, 0]) == 1
    True
    >>> solve(5, 2, [1, 0, 1, 1, 0]) == 1
    True
    >>> solve(5, 2, [1, 0, 1, 1, 1]) == 1
    True
    >>> solve(5, 2, [1, 1, 1, 1, 1]) == 0
    True
    """

def solve(n, r, a):
    ans = 0
    i = 1
    while i <= n:
        if a[i-1] == 0:
            j = i
            while j <= n and a[j-1] == 0:
                j += 1
            if j - i > 2*r:
                return -1
            if j <= n:
                a[j-1] = 1
                ans += 1
            else:
                return -1
            i = j
        else:
            i += 1
    return ans

def main():
    n, r, a = get_input(open('input.txt', 'r'))
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
