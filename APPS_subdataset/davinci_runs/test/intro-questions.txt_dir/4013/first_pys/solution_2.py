

def instability(a):
    return max(a) - min(a)

n = int(input())
a = list(map(int, input().split()))

# solution 1:
# instability_min = instability(a)
# for i in range(n):
#     a_temp = a[:i] + a[i+1:]
#     instability_temp = instability(a_temp)
#     if instability_temp < instability_min:
#         instability_min = instability_temp
# print(instability_min)

# solution 2:
a_min = min(a)
a_max = max(a)
if a.count(a_min) > 1:
    instability_min = a_max - a_min
else:
    instability_min = a_max - a_min
    a.remove(a_min)
    a_new_max = max(a)
    instability_min = min(instability_min, a_new_max - a_min)

if a.count(a_max) > 1:
    instability_min = min(instability_min, a_max - a_min)
else:
    instability_min = min(instability_min, a_max - a_min)
    a.remove(a_max)
    a_new_min = min(a)
    instability_min = min(instability_min, a_max - a_new_min)
print(instability_min)