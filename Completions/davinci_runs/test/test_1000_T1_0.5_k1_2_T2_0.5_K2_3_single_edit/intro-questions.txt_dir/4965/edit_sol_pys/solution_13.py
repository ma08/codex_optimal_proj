

n = int(input())
temps = list(map(int,input().split()))

# sort the temperatures
temps.sort()

# check if the temperature difference is increasing (only works for temps in range [-100,100])
# inc = True
# for i in range(1,n-1):
#     if abs(temps[i-1]-temps[i]) > abs(temps[i]-temps[i+1]):
#         inc = False
#         break

# if inc:
#     print(*temps)
# else:
#     print("impossible")

# this is the optimal solution
print(*temps)
