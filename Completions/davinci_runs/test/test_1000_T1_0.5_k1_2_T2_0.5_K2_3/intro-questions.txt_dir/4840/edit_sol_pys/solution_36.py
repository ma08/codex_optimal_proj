from collections import defaultdict


n = int(input())

def get_prob_sum(a, b):
    return (1 / (b - a + 1))

def get_prob(a, b, c, d):
    p_sum = 0
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            p_sum += get_prob_sum(i, b) * get_prob_sum(j, d)
    return p_sum

d = defaultdict(list)
for i in range(n):
    a, b, c, d = [int(x) for x in input().split()]
    d[i] = [a, b, c, d]

g_prob = 0
e_prob = 0

for key, val in d.items():
    if key == 0:
        g_prob += get_prob(val[0], val[1], val[2], val[3])
    else:
        e_prob += get_prob(val[0], val[1], val[2], val[3])

if g_prob > e_prob:
    print("Gunnar")
elif g_prob < e_prob:
    print("Emma")
else:
    print("Tie")
