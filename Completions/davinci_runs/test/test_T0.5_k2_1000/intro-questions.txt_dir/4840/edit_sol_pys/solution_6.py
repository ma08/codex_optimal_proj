

a1,b1,a2,b2 = [int(x) for x in input().split()] #Gunnar's first and second roll
c1,d1,c2,d2 = [int(x) for x in input().split()] #Emma's first and second roll

g = 0 #Gunnar's score
e = 0 #Emma's score

def get_prob(a, b):
    diff = b-a+1 #difference between a and b
    return (1/diff)
#Gunnar's first roll

    #Gunnar's second roll
for i in range(a1, b1+1):
        #Gunnar's score
    for j in range(a2, b2+1):
        if i+j > c1+c2+d1+d2:
            g += 1
        elif i+j < c1+c2+d1+d2:

#Emma's first roll
for i in range(c1, d1+1):
    #Emma's second roll
    for j in range(c2, d2+1):
        #Emma's score
        if i+j > a1+a2+b1+b2:
            e += 1
        elif i+j < a1+a2+b1+b2:
            g += 1

            e += 1

if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")
