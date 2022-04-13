#提出 #1710
#A - Shik and Stone Game
n = int(input())
a = list(map(int,input().split()))
if sum(a) % 2 == 0:
    print("YES")
else:
    print("NO")


#提出 #1711
#B - Easy Linear Programming
n,r = map(int,input().split())
if n < 10:
    print(r+100*(10-n))
else:
    print(r)
