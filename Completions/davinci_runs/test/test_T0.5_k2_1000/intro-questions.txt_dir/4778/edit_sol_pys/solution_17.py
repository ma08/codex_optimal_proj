

import sys

def main():
    line = sys.stdin.readline()
    P, D = list(map(int, line.split())) # P = number of precincts, D = number of districts
    precincts = []
    for i in range(P):
        line = sys.stdin.readline()
        d, a, b = list(map(int, line.split())) # d = district number, a = votes for A, b = votes for B
        precincts.append((d, a, b)) # precincts is a list of tuples
    districts = [None] * D
    for i in range(D):
        districts[i] = [] # districts is a list of lists
    for i in range(P):
        districts[precincts[i][0] - 1].append(precincts[i]) # precincts are added to their respective districts
    efficiency_gap = 0
    for i in range(D):
        district = districts[i]
        P = len(district) # number of precincts in district
        V = 0 # total votes in district
        w_A = 0 # wasted votes for A
        w_B = 0 # wasted votes for B
        for j in range(P):
            V += district[j][1] + district[j][2] # V = sum of votes for A and votes for B
        A_votes = 0 # votes for A
        B_votes = 0 # votes for B
        for j in range(P):
            A_votes += district[j][1] # A_votes = sum of votes for A
            B_votes += district[j][2] # B_votes = sum of votes for B
        if A_votes > B_votes:
            w_B = B_votes # wasted votes for B = votes for B
            if A_votes > V/2 + 1:
                w_A = A_votes - V/2 - 1 # wasted votes for A = votes for A - (V/2 + 1)
            else:
                w_A = 0 # wasted votes for A = 0
            print('A', int(w_A), int(w_B))
        else:
            w_A = A_votes # wasted votes for A = votes for A
            if B_votes > V/2 + 1:
                w_B = B_votes - V/2 - 1 # wasted votes for B = votes for B - (V/2 + 1)
            else:
                w_B = 0 # wasted votes for B = 0
            print('B', int(w_A), int(w_B))
        efficiency_gap += abs(w_A - w_B) # efficiency_gap = sum of absolute value of wasted votes for A - wasted votes for B
    efficiency_gap /= D # efficiency_gap = efficiency_gap / D
    print('{:.12f}'.format(efficiency_gap))

main()
