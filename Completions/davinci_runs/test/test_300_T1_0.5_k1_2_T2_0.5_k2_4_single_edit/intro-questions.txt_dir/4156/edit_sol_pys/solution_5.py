
# n,w=map(int,input().split())
# a=list(map(int,input().split()))
# if sum(a)>w or sum(a)<-w or sum(a)+w<0 or sum(a)-w>0:
#     print(0)
# else:
#     print(w-abs(sum(a)))

n = int(input())
s = input()
t = input()
i = 0
while i < n:
    if s[i] == t[i]:
        i += 1
    else:
        if i + 1 < n and s[i + 1] == t[i + 1]:
            i += 2
        else:
            i += 1
print(n - i)
