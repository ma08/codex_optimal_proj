
import math

def main():
    n = int(input())
    arr = list(map(int, input().split()))


    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                s = arr[i] + arr[j] + arr[k]
                if s % 2 == 0 and s > max_value:
                    max_value = s

    print(max_value)
    return


if __name__ == "__main__":
    main()
