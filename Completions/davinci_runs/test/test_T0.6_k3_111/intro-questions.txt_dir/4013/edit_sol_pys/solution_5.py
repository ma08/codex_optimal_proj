

def instability(a):
    return max(a) - min(a)

n = int(input())
a = list(map(int, input().split()))

# solution 1:
# instability_max = instability(a)
# for i in range(n):
#     a_temp = a[:i] + a[i+1:]
#     instability_temp = instability(a_temp) # instability_temp is the instability of the new array
#     if instability_temp < instability_max:
#         instability_max = instability_temp
# print(instability_max)

# solution 2:
a_min = min(a)
a_max = max(a)
if a.count(a_min) > 1:
    instability_max = a_max - a_min # instability_max is the instability of the new array
else:
    instability_max = a_max - a_min # instability_max is the instability of the new array
    a.remove(a_min)
    a_new_max = max(a)
    instability_max = min(instability_max, a_new_max - a_min) # instability_max is the instability of the new array

if a.count(a_max) > 1:
    instability_max = min(instability_max, a_max - a_min) # instability_max is the instability of the new array
else:
    instability_max = min(instability_max, a_max - a_min) # instability_max is the instability of the new array
    a.remove(a_max)
    a_new_min = min(a)
    instability_max = min(instability_max, a_max - a_new_min) # instability_max is the instability of the new array
print(instability_max)
