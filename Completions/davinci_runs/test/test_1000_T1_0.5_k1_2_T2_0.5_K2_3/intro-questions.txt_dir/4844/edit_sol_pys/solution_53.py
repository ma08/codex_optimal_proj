

def main():
    n = int(raw_input())
    i = 0
    j = 0
    arr = []
    while i < n:
        arr.append(list(map(int, raw_input().split())))
        i += 1
    res = [0] * n
    while j < n:
        res[j] = arr[j][0]
        j += 1
    i = 1
    while i < n:
        res[i] = arr[0][i]
        i += 1
    i = 1
    while i < n:
        j = 1
        while j < n:
            if i != j:
                res[i] = res[i] ^ arr[i][j]
            j += 1
        i += 1
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
