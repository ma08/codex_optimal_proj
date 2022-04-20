

from collections import defaultdict

n       = int(input())
strings = [input() for _ in range(n)]

# sort strings by length
strings.sort(key=lambda x: len(x))

# sort strings by lexicographical order
strings.sort()

# check if strings can be reordered
for i in range(n - 1):
    if strings[i] not in strings[i + 1]:
        print("NO")
        quit()

print("YES")
print("\n".join(strings))