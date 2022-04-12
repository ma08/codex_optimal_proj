
n = int(input()) # number of elements
a = list(map(int, input().split())) # list of elements

s = sum(a) # sum of elements

def is_good(a): # check if element is good
    for i in range(len(a)): # for each element
        if a[i] == sum(a[:i]) + sum(a[i+1:]): # if it is good
            return True
    return False

res = [] # list of good elements
for i in range(n): # for each element
    if is_good(a[:i] + a[i+1:]): # if it is good
        res.append(i+1)

print(len(res)) # print number of good elements
print(*res) # print good elements
