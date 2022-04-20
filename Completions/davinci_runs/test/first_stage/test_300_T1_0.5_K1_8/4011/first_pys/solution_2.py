

n = int(input())
a = input()
f = [int(x) for x in input().split()]

a_list = [int(x) for x in a]

# create a list of tuples
a_list_tuples = [(x, i) for i, x in enumerate(a_list)]

# sort the list of tuples
a_list_tuples = sorted(a_list_tuples, key=lambda x: f[x[0]-1])

# create a list of tuples for the sorted list of tuples
# this will help us find the index of the element in the original list
a_list_tuples_sorted = [(x, i) for i, x in enumerate(a_list_tuples)]

# sort the list of tuples by the original index
a_list_tuples_sorted = sorted(a_list_tuples_sorted, key=lambda x: x[1])

# get a list of the values of the sorted list of tuples
a_list_sorted = [x[0] for x in a_list_tuples_sorted]

# get the index of the first element in the sorted list which is not the same as the original list
for i in range(n):
    if a_list[i] != a_list_sorted[i]:
        break

# if the index is the last element, we are done
if i == n-1:
    print(a)
else:
    # otherwise, change the first element of the sorted list which is not the same as the original list
    a_list_sorted[i] = a_list[i]
    print(''.join([str(x) for x in a_list_sorted]))