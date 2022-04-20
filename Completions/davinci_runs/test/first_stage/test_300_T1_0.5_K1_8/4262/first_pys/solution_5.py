

# This solution is not optimal, but it works.
# I'm sure there's a better way to do this, but I don't know it, so I'll just leave this here.

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

p_index = 0
q_index = 0

for i in range(1, n + 1):
    if p[i - 1] == i:
        p_index += 1
    if q[i - 1] == i:
        q_index += 1

print(abs(p_index - q_index))