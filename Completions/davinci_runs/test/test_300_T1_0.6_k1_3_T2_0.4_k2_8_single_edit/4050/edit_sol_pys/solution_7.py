

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sums = {0: 1}
    s = 0
    ret = 1
    for i in range(n):
        s += arr[i]
        sums[s] = sums.get(s, 0) + 1
        ret = max(ret, sums[s])
    print(ret)

if __name__ == '__main__':
    main()
