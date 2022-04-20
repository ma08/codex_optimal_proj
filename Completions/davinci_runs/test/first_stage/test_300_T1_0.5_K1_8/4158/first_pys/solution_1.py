


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = []
    i = 0
    while i < n:
        result.append(arr[i])
        j = i + 1
        while j < n and arr[j] - arr[i] < 10**9:
            if arr[j] - arr[i] == 2**(len(bin(arr[j] - arr[i])) - 3):
                result.append(arr[j])
                i = j
            j += 1
        i += 1
    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()