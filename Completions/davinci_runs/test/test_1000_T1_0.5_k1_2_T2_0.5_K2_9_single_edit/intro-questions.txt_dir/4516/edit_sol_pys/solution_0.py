

"""
My solution:

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    for i in range(1, n + 1):
        s = 0
        for j in range(m):
            s += abs(x[j] - i)
        print(s, end=' ')
    

if __name__ == "__main__":
    main()
"""

"""
Fastest solution:

n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(1,n+1):
    s=0
    for j in range(m-1):
        s+=abs(a[j]-i)
    print(s, end=" ")
"""
