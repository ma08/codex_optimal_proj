

a1,b1,a2,b2 = [int(x) for x in input().split()] # gunnar
c1,d1,c2,d2 = [int(x) for x in input().split()] # emma

g = 0 # gunnar
e = 0 # emma

def get_prob(a, b): # probability
    diff = b-a+1
    return (1/diff)

for i in range(a1, b1+1):
    for j in range(a2, b2+1):
        if i+j > c1+c2+d1+d2: # gunnar wins
            g += 1
        elif i+j < c1+c2+d1+d2: # emma wins
            e += 1

if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")
