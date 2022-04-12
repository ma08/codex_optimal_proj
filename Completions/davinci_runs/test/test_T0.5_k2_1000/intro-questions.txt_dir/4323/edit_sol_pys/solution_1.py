

def main():
    """
    This program is used to find the minimum number of songs to compress so that they all fit on a flash drive
    """
    n, m = [int(i) for i in input().split()]
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = [int(i) for i in input().split()]
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum <= m:
        print(0)
    elif b_sum > m:
        print(-1)
    else:
        i = 0
        while a_sum > m:
            a_sum -= a[i]-b[i]
            i += 1
        print(i)

if __name__ == "__main__":
    main()
