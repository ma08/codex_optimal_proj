
def check(arr,b):
    i = 0
    if b in arr:
        return 1
    if b == 1:
        return -1
    if b%2 == 1:
        return -1
    while i < b:
        i += arr[i]
    if i == b:
        return int(log2(b))+1
    else:
        return -1
from math import log2

def main():
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(q):
        b = int(input())
        print(check(arr,b))

if __name__ == "__main__":
    main()
