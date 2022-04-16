
import sys 
sys.setrecursionlimit(10**6) 

def main():
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print(0)
            t -= 1
            continue
        if a[0] < a[1]:
            a[0] = -a[0]
        for i in range(1, n - 1):
            if a[i] < a[i + 1] and a[i] < a[i - 1]:
                a[i] = -a[i]
        if a[n - 1] < a[n - 2]:
            a[n - 1] = -a[n - 1]
        print(sum(a))
        t -= 1


main()
