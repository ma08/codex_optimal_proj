

# N switches, M bulbs
N, M = map(int, input().split())

# k_i switches connected to bulb i
# s_{ij} is the number of the j-th switch connected to bulb i (1-indexed)
# p_i is the parity of the number of switches that are "on" among the switches connected to bulb i
k = [0] * M
s = [0] * M
p = [0] * M
for i in range(M):
    k[i], *s[i] = map(int, input().split())  # s_{ij}
p = list(map(int, input().split()))

# The number of combinations of "on" and "off" states of the switches that light all the bulbs
count = 0

# Try all combinations of "on" and "off" states of the switches
for i in range(2**N):
    # Check if all the bulbs are lighted
    lighted = True
    for j in range(M):
        # Count the number of switches that are "on" among the switches connected to bulb j
        on = 0
        for l in range(k[j]):
            if i & (1 << (s[j][l] - 1)):
                on += 1
        # Check if bulb j is lighted
        if on % 2 != p[j]:
            lighted = False
            break
    if lighted:
        count += 1

print(count)
