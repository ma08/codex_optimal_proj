

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0
    while len(arr) > 0:
        tmp = arr[-1]
        arr.pop()
        if tmp == 0:
            break
        while tmp > 0:
            tmp = tmp & (tmp - 1)
            res += 1
    print(res)

if __name__ == "__main__":
    main()