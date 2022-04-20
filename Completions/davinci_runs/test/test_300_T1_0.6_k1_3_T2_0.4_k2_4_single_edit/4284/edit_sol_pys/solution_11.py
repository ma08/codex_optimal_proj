
import sys

def play(k,n,a,b):
    if k < a and k < b:
        return -1
    if k < a:
        return k//b
    if k < a+b:
        return 1
    return (k-a)//b + 1

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        k,n,a,b = map(int,input().split())
        print(min(play(k,n,a,b),n))
