

def main():
    """
    This program is used to find the minimum number of songs to compress so that they all fit on a flash drive.
    """
    n, m = [int(i) for i in input().split()]
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = [int(i) for i in input().split()]
        a.append(a_i)
        b.append(b_i)
    # a.sort()
    # b.sort()
    if sum(a) <= m:
        print(0)
    elif sum(b) > m:
        print(-1)
    else:
        i = 0
        while sum(a) > m:
            a[i] = b[i]
            i += 1
        print(i)

if __name__ == "__main__":
    main()
