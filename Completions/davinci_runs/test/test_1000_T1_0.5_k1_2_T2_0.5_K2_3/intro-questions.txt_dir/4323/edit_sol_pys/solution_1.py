

def main():
    """
    This program is used to find the minimum number of songs to compress so that they all fit on a flash drive.
    """
    n, m = [int(i) for i in input().split()]
    a = [0] * n
    b = [0] * n
    c = [0] * n
    for _ in range(n):
        a_i, b_i = [int(i) for i in input().split()]
        a[i] = a_i
        b[i] = b_i
        c[i] = a_i - b_i
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum <= m:
        print(0)
    elif b_sum > m:
        print(-1)
    else:
        i = n-1
        while a_sum > m:
            a_sum -= c[i]
            i -= 1
        print(i)

if __name__ == "__main__":
    main()
