

def coloring(s):
    l = []
    c = 1
    l.append(c)
    for i in range(len(s)-1):        
        if s[i] != s[i+1]:            
            c+=1
        else:
            l.append(c)
    l.append(c)
    return l

n = int(input())
s = input()

print(max(coloring(s)))
print(*coloring(s))
