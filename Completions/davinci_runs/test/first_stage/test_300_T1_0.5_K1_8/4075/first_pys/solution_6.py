

# N: number of switches
# M: number of bulbs
# k_i: number of switches connected to bulb i
# s_ij: switch connected to bulb i
# p_i: 0/1 whether bulb i is lit by even/odd number of switches connected to it

# Input
N, M = map(int, input().split())
k_i = []
s_ij = []
p_i = []
for i in range(M):
    k_i.append(list(map(int, input().split()))[0])
    s_ij.append(list(map(int, input().split()))[1:])
    p_i.append(list(map(int, input().split()))[0])

# Solve
# The number of combinations of "on" and "off" states of the switches that light all the bulbs is the number of combinations of "on" and "off" states of the switches that light each bulb.
# Since the number of switches that are "on" among s_{i1}, s_{i2}, ..., and s_{ik_i} is congruent to p_i modulo 2, the number of combinations of "on" and "off" states of the switches that light bulb i is 2^{k_i-1}.
# The total number of combinations is therefore 2^{k_1-1} \times 2^{k_2-1} \times ... \times 2^{k_M-1}.
ans = 1
for i in range(M):
    ans *= 2**(k_i[i]-1)

# Output
print(ans)