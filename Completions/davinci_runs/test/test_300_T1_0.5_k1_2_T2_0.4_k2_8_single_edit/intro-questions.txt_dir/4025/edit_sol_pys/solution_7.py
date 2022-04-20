

n = int(input())
a = [int(x) for x in input().split()]
print(a.count(5)//9*9 + 5*(a.count(5)%9 > 0))
