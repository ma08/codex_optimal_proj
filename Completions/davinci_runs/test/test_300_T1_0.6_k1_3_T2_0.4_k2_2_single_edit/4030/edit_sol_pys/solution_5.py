

def coloring(s):
    l = []
    c = 1
    for i in range(len(s)-1): # check if the next char is different from the current one
        if s[i] != s[i+1]:
            l.append(c) # if it is, append the current count
            c+=1 # increment the count
        else:
            l.append(c)
    l.append(c)
    return l

n = int(input())
s = input()

print(max(coloring(s)))
print(*coloring(s))
