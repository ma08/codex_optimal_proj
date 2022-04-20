

def coloring(s):
    l = []
    c = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            l.append(c)
            c = 1
        else:
            c+=1
    l.append(c)    
    return l

n = int(input())
s = input()

print(max(coloring(s)))
print(*coloring(s))
