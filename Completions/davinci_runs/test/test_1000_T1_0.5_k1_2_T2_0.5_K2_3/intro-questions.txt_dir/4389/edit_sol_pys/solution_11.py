def main():
    a = input()
    b = a.split()
    n = int(b[0])
    m = int(b[1])
    l = int(b[2])
    r = int(b[3])
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(m):
            arr[i].append(0)
    i = 0
    j = 0
    while l <= r:
        if i % 2 == 0:
            while j < m:
                arr[i][j] = l
                l += 1
                j += 1
        else:
            while j >= 0:
                arr[i][j] = l
                l += 1
                j -= 1
        i += 1
        j += 1
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
