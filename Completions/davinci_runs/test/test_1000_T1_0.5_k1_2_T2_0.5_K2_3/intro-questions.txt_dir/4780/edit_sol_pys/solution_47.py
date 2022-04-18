

# SOLUTION

# Read input and reverse lists if needed.
a = [x for x in input()]  # noqa
b = [x for x in input()]  # noqa
t = int(input())  # noqa
if t % 2 == 1:  # noqa
    a, b = b, a  # noqa

# Swap ants.
for i in range(t // 2):  # noqa
    a.insert(i + 1, b[i])  # noqa
    b.insert(i + 1, a[-i - 1])  # noqa
    a.pop(-i - 1)  # noqa
    b.pop(i)  # noqa

# Print result.
print(''.join(a + b))  # noqa
