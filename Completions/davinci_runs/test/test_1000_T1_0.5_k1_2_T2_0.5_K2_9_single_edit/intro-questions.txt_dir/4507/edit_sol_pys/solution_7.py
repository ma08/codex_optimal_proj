

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    while True:
        if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
            break
        arr.sort()
        cnt += 1
        if arr[0][0] < arr[1][0]:
            arr[0][0] += 1
            arr[0][1] += 1
        else:
            arr[1][0] += 1
            arr[1][1] += 1
    print(cnt)

if __name__ == "__main__":
    main()
