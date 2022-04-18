

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    res = [0] * m
    for i in range(m):
        res[i] = arr[i % n]
        arr[i % n] += 1
    print(sum(res))
    print(' '.join(map(str, res)))


if __name__ == "__main__":
    main()
