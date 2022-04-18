

#This solution is incredibly slow, but it works. It uses
# brute force to find all possible combinations.

b, d, c, l = map(int, input().split()) #input

def solve(b, d, c, l):
    if b + d + c > l:
        return None #if the sum is greater than the length
    if b + d + c == l:
        return [b, d, c]
    return None #if the sum is equal to the length

solutions = []
#loop to find all possible combinations
for i in range(l//b + 1):
    for j in range(l//d + 1):
        for k in range(l//c + 1):
            if i * b + j * d + k * c == l:
                solutions.append([i, j, k])

if len(solutions) == 0: #if there are no solutions
    print("impossible") #print impossible
else:
    for i in sorted(solutions): #sorts the list
        print(i[0], i[1], i[2]) #prints the solutions
