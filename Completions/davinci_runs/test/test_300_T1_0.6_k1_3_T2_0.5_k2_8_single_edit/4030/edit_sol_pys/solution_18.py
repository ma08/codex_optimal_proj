

def coloring(s):
    l = []
    for i in s:
        if i == 'R':
            l.append(0)
        else:
            l.append(1)
    return l

n = int(input())
s = input()

print(len(s))
print(*coloring(s),sep="")
