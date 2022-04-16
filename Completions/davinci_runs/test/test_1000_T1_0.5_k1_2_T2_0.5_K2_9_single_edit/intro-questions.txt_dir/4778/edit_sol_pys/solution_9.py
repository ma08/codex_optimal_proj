

import sys

def main():
    line = sys.stdin.readline()
    P, D = list(map(int, line.split()))
    precincts = []
    for i in range(P):
        line = sys.stdin.readline()
        d, a, b = list(map(int, line.split()))
        precincts.append((i, d, a, b))
    districts = [None] * D
    for i in range(D):
        districts[i] = []
    for i in range(P):
        districts[precincts[i][1] - 1].append(precincts[i])
    efficiency_gap = 0
    for i in range(D):
        district = districts[i]
        precinct_count = len(district)
        V = 0
        wasted_A = 0
        wasted_B = 0
        for j in range(precinct_count):
            V += district[j][2] + district[j][3]
        A_votes = 0
        B_votes = 0
        for j in range(precinct_count):
            A_votes += district[j][2]
            B_votes += district[j][3]
        if A_votes > B_votes:
            wasted_B = B_votes
            if A_votes > V/2 + 1:
                wasted_A = A_votes - V/2 - 1
            else:
                wasted_A = 0
            print('A', int(wasted_A), int(wasted_B))
        else:
            wasted_A = A_votes
            if B_votes > V/2 + 1:
                wasted_B = B_votes - V/2 - 1
            else:
                wasted_B = 0
            print('B', int(wasted_A), int(wasted_B))
        efficiency_gap += abs(wasted_A - wasted_B)
    efficiency_gap /= V
    print('{:.12f}'.format(efficiency_gap))

main()
