
s = input()

# count the number of black tiles
counter = 0
for c in s:
    if c == '0':
        counter += 1
print(counter)
