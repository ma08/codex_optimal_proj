

r, n = map(int, input().split()) # r: range, n: size of array

for i in range(1, r+1): # i: index
    if i not in map(int, input().split()): # if i is not in array
        print(i) # print i
        break # stop the loop
else:
    print("too late")
