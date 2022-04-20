import heapq

sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
import sys

def main():
    N,M,K=LI()
    A=LI()
    B=LI()
    a=[]
    b=[]
    for i in range(N):
        a.append((A[i],i))
    for i in range(M):
        b.append((B[i],i))
    a.sort(reverse=True)
    b.sort(reverse=True)
    cnt=0
    res=[]
    for i in range(N):
        for j in range(M):
            if a[i][0]+b[j][0]<K:
                break
            if a[i][1]>b[j][1]:
                res.append((a[i][1],b[j][1]))
                cnt+=1
    print(cnt)
    res.sort(key=lambda x:x[0])
    for r in res:
        print(r[0]+1,r[1]+1)
if __name__ == '__main__':
    main()
