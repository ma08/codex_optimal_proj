

a1,b1,a2,b2 = [int(x) for x in input().split()]
c1,d1,c2,d2 = [int(x) for x in input().split()]

g = 0
e = 0

def get_prob(a, b):
    diff = b-a+1
    return (1/diff)

for i in range(a1, b1+1):
    for j in range(a2, b2+1):
        if i+j > c1+c2+d1+d2:
            g += 1
        elif i+j < c1+c2+d1+d2:
            e += 1
print(g, e)


if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")
