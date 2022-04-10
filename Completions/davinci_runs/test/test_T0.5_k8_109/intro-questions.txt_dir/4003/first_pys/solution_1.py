

#-----SOLUTION-----

n = int(input())
a = list(map(int, input().split()))

# We will first use a greedy approach to find the first L or R that can be added to our solution
# If there is no L or R such that it can be added to our solution, then we can just add the last element to our solution

ans = []
while a:
    if not ans:
        # If ans is empty, then we can just add the first element to our solution
        ans.append(a[0])
        a.pop(0)
    elif len(a) == 1:
        # If there is only one element left, then we can just add it to our solution
        ans.append(a[0])
        a.pop(0)
    else:
        # If the first element is greater than the last element in our solution, then we can add it to our solution
        if a[0] > ans[-1]:
            ans.append(a[0])
            a.pop(0)
        # If the last element is greater than the last element in our solution, then we can add it to our solution
        elif a[-1] > ans[-1]:
            ans.append(a[-1])
            a.pop()
        # If neither the first element nor the last element is greater than the last element in our solution, then we can just add the last element to our solution
        else:
            ans.append(a[-1])
            a.pop()

# Now we need to find the longest strictly increasing subsequence in ans

# We will first use a greedy approach to find the first L or R that can be added to our solution
# If there is no L or R such that it can be added to our solution, then we can just add the last element to our solution

ans2 = []
while ans:
    if not ans2:
        # If ans is empty, then we can just add the first element to our solution
        ans2.append(ans[0])
        ans.pop(0)
    elif len(ans) == 1:
        # If there is only one element left, then we can just add it to our solution
        ans2.append(ans[0])
        ans.pop(0)
    else:
        # If the first element is greater than the last element in our solution, then we can add it to our solution
        if ans[0] > ans2[-1]:
            ans2.append(ans[0])
            ans.pop(0)
        # If the last element is greater than the last element in our solution, then we can add it to our solution
        elif ans[-1] > ans2[-1]:
            ans2.append(ans[-1])
            ans.pop()
        # If neither the first element nor the last element is greater than the last element in our solution, then we can just add the last element to our solution
        else:
            ans2.append(ans[-1])
            ans.pop()

print(len(ans2))
for i in ans2:
    if i == ans[0]:
        print('L', end='')
    else:
        print('R', end='')