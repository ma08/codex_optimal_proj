

def main():
    n = int(input())
    i = 1
    j = 1
    arr = []
    while i < n:
        arr.append(list(map(int, input().split())))
        i += 1
    res = [0] * n
    while j < n:
        res[j] = arr[j][1]
        j += 1
    res[0] = arr[0][1]
    while i < n:
        res[0] = res[0] ^ arr[i][0]
        i += 1
    i = 2
    while i < n:
        j = 2
        while j < n:
            if i != j and arr[i][j] == 1:
                res[i] = res[i] ^ arr[i][j]
            j += 1
        i += 1
    print(*res, sep=' ')

if __name__ == "__main__":
    main()
