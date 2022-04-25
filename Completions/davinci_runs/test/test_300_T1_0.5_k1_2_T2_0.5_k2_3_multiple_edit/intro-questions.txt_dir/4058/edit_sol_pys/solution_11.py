
def get_input():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    return n, r, a

    """
    >>> solve(5, 2, [1, 0, 0, 0, 1])
    2
    >>> solve(5, 2, [1, 0, 0, 0, 0])
    -1
    >>> solve(5, 2, [1, 1, 0, 0, 0])
    -1
    >>> solve(5, 2, [0, 0, 0, 0, 0])
    -1
    >>> solve(5, 2, [0, 0, 0, 0, 1])
    1
    >>> solve(5, 2, [1, 0, 1, 0, 1])
    0
    >>> solve(5, 2, [1, 0, 1, 0, 0])
    1
    >>> solve(5, 2, [1, 0, 1, 1, 0])
    1
    >>> solve(5, 2, [1, 0, 1, 1, 1])
    1
    >>> solve(5, 2, [1, 1, 1, 1, 1])
    0
    """
def solve(n, r, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            first_zero = i
            while i < n and a[i] == 0:
                i += 1
            last_zero = i
            if last_zero - first_zero > 2*r:
                return -1  # impossible to make every room happy
            if last_zero < n:
                a[last_zero] = 1  # make the last_zero-th room happy
                ans += 1  # you need to visit the last_zero-th room
            else:
                return -1  # impossible to make every room happy
        else:
            i += 1
    return ans  # number of visits

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
