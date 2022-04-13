

a1, b1, c1, d1 = [int(x) for x in input().split()]
a2, b2, c2, d2 = [int(x) for x in input().split()]

g_win = 0
e_win = 0

def get_prob(a, b):
    diff = b-a+1
    return (1/diff)

for i in range(a1, b1+1):
    for j in range(a2, b2+1):
        if i+j > c1+c2+d1+d2:
            g_win += 1
        elif i+j < c1+c2+d1+d2:
            e_win += 1

if g_win > e_win:
    print("Gunnar")
elif g_win < e_win:
    print("Emma")
else:
    print("Tie")
