

def main():
    n = int(input('Enter the number of elements: '))
    arr = list(map(int, input('Enter the elements: ').split()))
    sums = {}
    ret = 1
    for i in range(n):
        for j in range(i, n):
            s = sum(arr[i:j + 1])
            sums[s] = sums.get(s, 0) + 1
            ret = max(ret, sums[s])
    print(ret)
    for i in range(n):
        for j in range(i, n):
            s = sum(arr[i:j + 1])
            if sums[s] == ret:
                ret -= 1
                print(i + 1, j + 1)
                break

if __name__ == '__main__':
    main()
