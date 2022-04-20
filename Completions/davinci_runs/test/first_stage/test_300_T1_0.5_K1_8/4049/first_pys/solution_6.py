

#SOLUTION

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def win(a,b):
    if a == 1 and b == 2:
        return 1
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 1
    else:
        return 0

min_win = 0
for i in range(1,4):
    for j in range(1,4):
        min_win += min(a[i-1],b[j-1])*win(i,j)

max_win = 0
for i in range(1,4):
    for j in range(1,4):
        max_win += max(a[i-1],b[j-1])*win(i,j)

print(min_win,max_win)