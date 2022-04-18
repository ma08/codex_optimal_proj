
# SOLUTION

# Read input and reverse lists if needed
a = [x for x in input()]
b = [x for x in input()]
t = int(input())
if t % 2 == 1:
    a, b = b, a

# Swap ants
for i in range(t // 2):
    a.insert(i + 1, b[i])
    b.insert(i + 1, a[-i - 1])
    a.pop(-i - 1)
    b.pop(i)

# Print result
print(''.join(a + b))
