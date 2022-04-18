
n,a = map(int,input().split()) # taking input
e = list(map(int,input().split())) # taking input

e.sort() # sorting the elements

#print(e)

i = 0 # starting index
j = n-1 # last index

res = 0 # final answer

while i <= j: # checking if the element is greater than the other
    if e[i] >= e[j]:
        if a >= e[i]: # checking if the element fits in the bag
            a -= e[i]
            e[i] = 0 # making the element zero
            i += 1
        else: # if it doesn't fit in the bag break
            break
    else:
        if a >= e[j]: # checking if the element fits in the bag
            a -= e[j]
            e[j] = 0
            j -= 1
        else:
            break

#print(e)

for i in range(n):
    if e[i] == 0:
        res += 1

print(res)
