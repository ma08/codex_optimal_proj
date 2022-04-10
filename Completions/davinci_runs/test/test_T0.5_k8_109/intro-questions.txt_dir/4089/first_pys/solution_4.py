

n = int(input())

# 1. find the length of the name
# 2. find the number of names of the length
# 3. find the name of the length

# 1.
l = 0
i = 0
while True:
    i += 26**l
    if n <= i:
        break
    l += 1

# 2.
num = 0
for j in range(1, l+1):
    num += 26**j

# 3.
n -= num

# 4.
name = ''
while True:
    temp = chr(n % 26 + 97)
    name = temp + name
    n = int(n / 26)
    if n == 0:
        break

print(name)