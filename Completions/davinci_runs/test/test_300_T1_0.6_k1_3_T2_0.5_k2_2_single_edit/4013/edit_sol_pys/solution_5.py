
n = int(input())
array = list(map(int, input().split()))
array.sort()
min_instability = array[-1] - array[0]
for i in range(1, n-1):
    if array[i] - array[i-1] < min_instability:
        min_instability = array[i] - array[i-1]
    if array[i+1] - array[i] < min_instability:
        min_instability = array[i+1] - array[i]
print(min_instability)
