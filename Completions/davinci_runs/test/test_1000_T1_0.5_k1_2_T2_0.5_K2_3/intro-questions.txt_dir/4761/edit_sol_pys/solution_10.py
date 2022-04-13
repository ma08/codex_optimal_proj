

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    def mean():
        return sum(arr) / n

    def median():
        arr.sort()
        if n % 2 == 0:
            return (arr[n // 2] + arr[n // 2 - 1]) // 2
        else:
            return arr[n // 2]

    def mode():
        mode = arr[0]
        max_occurrences = 1
        for i in range(1, n):
            occurrences = 0
            for j in range(i, n):
                if arr[i] == arr[j]:
                    occurrences += 1
                if occurrences > max_occurrences:
                    mode = arr[i]
                    max_occurrences = occurrences
        return mode

    print(mean())
    print(median())
    print(mode())

if __name__ == "__main__":
    main()
