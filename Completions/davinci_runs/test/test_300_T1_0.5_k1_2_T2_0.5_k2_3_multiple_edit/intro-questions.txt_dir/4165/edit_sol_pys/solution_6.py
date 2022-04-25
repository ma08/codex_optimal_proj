n = int(input())
li = list(map(int, input().split()))
if max(li) < sum(li)-max(li):
    print("Yes")
else:
    print("No")
