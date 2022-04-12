

import sys

def main():
    line = sys.stdin.readline()
    P, D = list(map(int, line.split()))
    precincts = [None] * P
    for i in range(P):
        line = sys.stdin.readline()
        d, a, b = list(map(int, line.split()))
        precincts[i] = (d, a, b)
    districts = [None] * D
    for i in range(D):
        districts[i] = []
    for i in range(P):
        districts[precincts[i][0] - 1].append(precincts[i])
    efficiency_gap = 0
    for i in range(D):
        district = districts[i]
        P = len(district)
        V = 0
        w_A = 0
        w_B = 0
        for j in range(P):
            V += district[j][1] + district[j][2]
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
