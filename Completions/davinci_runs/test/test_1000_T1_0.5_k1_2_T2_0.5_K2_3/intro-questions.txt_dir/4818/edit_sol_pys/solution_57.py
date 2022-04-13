

def main():
    n, m = map(int, input().split())  # read a line with a single integer
    a = list(map(int, input().split()))  # read a list of integers, 2 in this case
    b = list(map(int, input().split()))  # read a list of integers, 2 in this case


    a.sort()
    b.sort()

    best = 0
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            best += 1
            i += 1
        j += 1
    print(best)


if __name__ == '__main__':
    main()
