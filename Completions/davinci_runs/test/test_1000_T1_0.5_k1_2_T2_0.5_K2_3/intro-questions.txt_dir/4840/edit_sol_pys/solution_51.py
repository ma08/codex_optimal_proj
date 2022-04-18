

g = [1,4,1,4]
#g = [1,8,1,8]
#e = [1,6,1,6]
e = [1,10,2,5]

g_ranges = [[g[0],g[1]],[g[2],g[3]]]
e_ranges = [[e[0],e[1]],[e[2],e[3]]]

g_win = 0
e_win = 0

for i in range(g_ranges[0][0],g_ranges[0][1]+1):
    for j in range(g_ranges[1][0],g_ranges[1][1]+1):
        for k in range(e_ranges[0][0],e_ranges[0][1]+1):
            for l in range(e_ranges[1][0],e_ranges[1][1]+1):
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
