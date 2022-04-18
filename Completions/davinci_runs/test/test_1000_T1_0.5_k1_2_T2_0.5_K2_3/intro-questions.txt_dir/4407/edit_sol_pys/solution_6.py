
from math import log2

def main():
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(q):
        b = int(input())
        i = 0
        if b in arr:
            print(1)
            continue
        if b == 1:
            print(-1)
            continue
        #if b%2 == 1:
        #    print(-1)
        #    continue
        while i < b:
            i += arr[i]
        if i == b:
            print(int(log2(b))+1)
        else:
            print(-1)

if __name__ == "__main__":
    main()
