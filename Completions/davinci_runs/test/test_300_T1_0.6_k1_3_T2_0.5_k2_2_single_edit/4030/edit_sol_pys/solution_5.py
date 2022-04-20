

def coloring(s):
    count = 1
    color = [1]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            count += 1
        color.append(count)
    return color

n = int(input())
s = input()

print(max(coloring(s)))
print(*coloring(s))
