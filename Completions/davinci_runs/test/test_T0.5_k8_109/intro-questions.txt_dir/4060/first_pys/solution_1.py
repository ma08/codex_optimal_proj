

n = int(input())
s = input()

# неправильные открывающие скобки
count = 0
# неправильные закрывающие скобки
result = 0

for i in range(n):
    if s[i] == '(':
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            result += 1

print(result)