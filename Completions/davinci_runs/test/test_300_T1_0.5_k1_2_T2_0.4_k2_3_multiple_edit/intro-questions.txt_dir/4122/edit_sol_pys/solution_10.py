import math

def main():
    n = int(input())
    arr = list(map(int, input().split())) # [1, 2, 3, 4, 5]

    print(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)


if __name__ == "__main__":
    main()
