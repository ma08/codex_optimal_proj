
x = int(input()) # number of elements in the array
s = input() # the array

w = 0 # number of W's in the array
m = 0 # number of M's in the array
i = 0 # number of elements in the array

for c in s:
    if c == 'W': # if the element is W
        w += 1
    else: # if the element is M
        m += 1
    if abs(w - m) > x: # if the difference between the number of W's and M's is greater than x
        break
    i += 1 # increment the number of elements in the array

print(i)
