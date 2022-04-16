

from math import log2

def main():
    n,_ = map(int,input().split())
    arr = list(map(int,input().split()))
    while True:
        b = int(input())
        i = 0
        if b == 0:
            break
        if b in arr or b == 1 or b%2 == 1:
            print(-1)
            continue
        while i < b:
            i += arr[i]
        if i == b:
            print(int(log2(b)+1))
        else:
            print(-1)

if __name__ == "__main__":
    main()
