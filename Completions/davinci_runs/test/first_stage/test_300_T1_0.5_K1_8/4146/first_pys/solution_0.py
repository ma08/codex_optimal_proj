

import sys

n = int(input())
l = list(map(int, input().split()))

# Count of each number in the list
count_dict = {}
for i in l:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

# If there are 3 or more different numbers, we can't make it /\/\/\/
if len(count_dict) >= 3:
    print(-1)
    sys.exit()

# If there are only 2 different numbers, we can make it /\/\/\/ by replacing the number that appears less
elif len(count_dict) == 2:
    print(n//2 - min(count_dict.values()))

# If there is only 1 different number, we can make it /\/\/\/ by replacing all of them
else:
    print(n)