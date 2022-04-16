

# get number of elements
n = int(input())
# get elements
l = list(map(int, input().split()))

# get number of queries
q = int(input())
# get queries
q_list = []
for i in range(q):
    q_list.append(list(map(int, input().split())))

# create an empty list to store the results
results = []
# execute queries
for i in range(q):
    # get the sum of the elements in the range
    s = sum(l[q_list[i][0]-1:q_list[i][1]])
    # append the result to the results list
    results.append(s)

# print results
for i in results:
    print(i)
