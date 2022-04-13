
g1 = [1,4,1,4]
e1 = [1,6,1,6]

g = [[g1[0],g1[1]],[g1[2],g1[3]]]
e = [[e1[0],e1[1]],[e1[2],e1[3]]]

g_win = 0
e_win = 0

for i in range(g[0][0],g[0][1]+1):
    for j in range(g[1][0],g[1][1]+1):
        for k in range(e[0][0],e[0][1]+1):
            for l in range(e[1][0],e[1][1]+1):
                if i+j > k+l:
                    g_win += 1
                elif i+j < k+l:
                    e_win += 1

if g_win > e_win:
    print("Gunnar") #Gunnar
elif g_win < e_win:
    print("Emma") #Emma
else:
    print("Tie") #Tie
