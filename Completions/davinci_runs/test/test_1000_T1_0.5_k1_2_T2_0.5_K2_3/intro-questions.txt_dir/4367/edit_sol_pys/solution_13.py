# #提出 #1709
# #A - Easy Linear Programming
# n,r = map(int,input().split())
# if n < 10:
#     print(r+100*(10-n))
# else:
#     print(r)

#提出 #1710
#A - Ehab and another construction problem
n = int(input())
for i in range(1,n+1):
    if i*i <= n:
        print(i,i)
    elif i*2 <= n:
        print(i,2)
    else:
        break
