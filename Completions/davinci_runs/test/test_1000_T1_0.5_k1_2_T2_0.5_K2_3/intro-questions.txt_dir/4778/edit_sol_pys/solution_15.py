

import sys

def main():
    line = sys.stdin.readline()
    P, D = list(map(int, line.split()))
    preceincts = []
    for i in range(P):
        line = sys.stdin.readline()
        d, a, b = list(map(int, line.split()))
        preceincts.append((d, a, b))
    districts = [[] for i in range(D)]
    for i in range(P):
        districts[preceincts[i][0] - 1].append(preceincts[i])
    efficiency_gap = 0
    for i in range(D):
        district = districts[i]
        V = sum([district[j][1] + district[j][2] for j in range(len(district))])
        A_votes = 0
        B_votes = 0
        for j in range(P):
            A_votes += district[j][1]
            B_votes += district[j][2]
        if A_votes > B_votes:
            w_B = B_votes
            if A_votes > V/2 + 1:
                w_A = A_votes - V/2 - 1
            else:
                w_A = 0
        else:
            w_A = A_votes
            if B_votes > V/2 + 1:
                w_B = B_votes - V/2 - 1
            else:
                w_B = 0
        efficiency_gap += abs(w_A - w_B)
    efficiency_gap /= V
    print('{:.12f}'.format(efficiency_gap))

main()
