
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    res = [0] * n
    for j in range(n):
        res[j] = arr[j][0]
    for i in range(1, n):
        res[i] = arr[0][i]
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                res[i] = res[i] ^ arr[i][j]
    print(*res)

if __name__ == "__main__":
    main()
