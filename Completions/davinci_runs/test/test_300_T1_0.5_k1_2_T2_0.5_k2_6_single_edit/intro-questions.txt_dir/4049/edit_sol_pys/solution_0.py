

from sys import stdin

def min_max_sum(arr):
    arr.sort()
    return sum(arr[:4]), sum(arr[1:])

def main():
    arr = list(map(int, stdin.readline().strip().split(" ")))
    print(" ".join(map(str, min_max_sum(arr))))

if __name__ == "__main__":
    main()
