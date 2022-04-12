
from collections import defaultdict

def main(N, M, P, S):
    acs = defaultdict(int)
    penalties = defaultdict(int)
    for i in range(M):
        if S[i] == 'AC':
            if acs[P[i]] == 0:
                acs[P[i]] = 1
        else:
            penalties[P[i]] += 1
    ac_count = sum(acs.values())
    penalty_count = sum([penalties[i] for i in penalties if acs[i] == 1])
    print(ac_count, penalty_count)

if __name__ == '__main__':
    N, M = map(int, input().split())
    P = [0]*M
    S = [0]*M
    for i in range(M):
        P[i], S[i] = input().split()
    main(N, M, P, S)
