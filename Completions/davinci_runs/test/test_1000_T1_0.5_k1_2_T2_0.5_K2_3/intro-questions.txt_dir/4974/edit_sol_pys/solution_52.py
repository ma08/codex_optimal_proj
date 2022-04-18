

# #%%
# r,n = map(int, input().split())
# rooms = set(range(1,r+1))
# booked = set(map(int, [input() for _ in range(n)]))
# rooms = rooms - booked
# if len(rooms) > 0:
#     print(min(rooms))
# else:
#     print("too late")

# #%%


# #%%


import math

n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list.sort()

for num in num_list:
    print(num)
