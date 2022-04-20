

# Solution

# Solution approach
'''
Iterate over the array, keeping track of the max value seen so far.
If the current element is greater than the max value, increment the answer
and update the max value.

Now, the array is sorted in decreasing order.
Iterate over the array again, keeping track of the max value seen so far.
If the current element is greater than the max value, increment the answer
and update the max value.

If there are multiple answers, you can print any.
'''


# Code
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
a = [int(x) for x in input().strip().split(' ')]

max_val = -1
ans = 0

for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
        ans += 1

a.sort(reverse=True)

max_val = -1

for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
        ans += 1

print(ans)

for i in range(n):
    if a[i] > max_val:
        print("L", end='')
        max_val = a[i]
    else:
        print("R", end='')