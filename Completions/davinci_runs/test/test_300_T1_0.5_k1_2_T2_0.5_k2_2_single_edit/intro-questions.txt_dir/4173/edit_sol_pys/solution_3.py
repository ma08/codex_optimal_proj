
#https://www.codechef.com/problems/SALARY
q = int(input())

for i in range(q):
    n = int(input())
    w = [int(x) for x in input().split()]
    print(min(w) * (n-1))
