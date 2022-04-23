

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sums = [0] * n
    s = 0
    for i in range(n):
        s += arr[i]
        sums[i] = s
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if sums[i] - sums[j] == k:
                print(j + 1, i)
                return
    print('-1')

if __name__ == '__main__':
    main()
