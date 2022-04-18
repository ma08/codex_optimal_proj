

n = int(input())
arr = list(map(int,input().split()))
max_ele = max(arr)
min_ele = min(arr)
arr.remove(max_ele)
arr.remove(min_ele)

print(max_ele,min_ele)
