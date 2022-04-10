
# Solution 

n = int(input())
arr = [int(x) for x in input().split()]
d = {}
for i in range(n):
    if arr[i] not in d.keys():
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1

new_arr = []
for k, v in d.items():
    new_arr.append(k)

print(len(new_arr))
for i in new_arr:
    print(i, end=" ")
