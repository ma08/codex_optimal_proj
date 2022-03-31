
n = int(input())
a = [int(x) for x in input().split()]

contestant = []

for i in range(n):
    
    if len(contestant) == 0:
        contestant.append(a[i])
    elif a[i] <= contestant[-1] * 2:
        contestant.append(a[i])
    else:
        contestant = [a[i]]

print(len(contestant))
