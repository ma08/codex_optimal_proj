

n = int(input())
s = input()

# Because we can swap any two neighboring characters of the string that are colored different colors.
# We can just sort the string by character.
# Then we can color the string by the sorted order.
s = sorted(s)

# Because we can swap any two neighboring characters of the string that are colored different colors.
# We can just color the string by the sorted order.
# Then we can sort the string by color.
c = [0] * n
for i in range(n):
    c[i] = s.index(s[i]) + 1

print(max(c))
print(*c)