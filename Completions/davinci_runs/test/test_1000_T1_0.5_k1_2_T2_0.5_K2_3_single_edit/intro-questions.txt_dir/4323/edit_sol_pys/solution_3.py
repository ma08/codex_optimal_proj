

def main():
    """
    This program is used to find the minimum number of songs to compress so that they all fit on a flash drive.


    """
    n, m = [int(i) for i in input().split()]
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    a_sum = sum(a)
    if a_sum <= m:
        print(0)
    else:
        i = 0
        while a_sum > m:
            a_sum -= a[i]
            i += 1
        print(i)

if __name__ == "__main__":
    main()
