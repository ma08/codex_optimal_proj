

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    res = [0] * n
    for j in range(n):
        res[j] = arr[j][0] ^ arr[0][j]
    for i in range(1, n):
        for j in range(1, n):
            if i != j and arr[i][j] == 1:
                res[i] = res[i] ^ 1
    print(*res)

if __name__ == "__main__":
    main()
