

from math import log2

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        b = int(input())
        j = 0
        if b in arr:
            print(1)
            continue
        if b == 1:
            print(-1)
            continue
        if b%2 == 1:
            print(-1)
            continue
        while j < b:
            j += arr[j]
        if j == b:
            print(int(log2(b))+1)
        else:
            print(-1)

if __name__ == "__main__":
    main()
