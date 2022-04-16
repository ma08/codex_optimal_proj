

from collections import defaultdict

def main(N, M, p, s):
    acs = defaultdict(int)
    penalties = defaultdict(int)
    for i in range(M):
        if s[i] == 'AC':
            if acs[p[i]] == 0:
                acs[p[i]] = 1
        else:
            penalties[p[i]] += 1
    ac_count = sum(acs.values())
    penalty_count = sum([penalties[i] for i in penalties if acs[i] == 1])
    print(ac_count, penalty_count)

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = [0]*M
    s = [0]*M
    for i in range(M):
        p[i], s[i] = input().split()
    main(N, M, p, s)
