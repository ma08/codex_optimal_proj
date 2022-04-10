

# SOLUTION

# input
s = input()
t = input()

# get the indexes of all letters of t in s
result = 0
for i in range(len(t)):
    result = max(result, s.index(t[i]) - i)

print(result)