

from collections import defaultdict

def main(N, M, p, S):
    ac_counts = defaultdict(int)
    penalties = defaultdict(int)
    for i in range(M):
        if S[i] == 'AC':
            if ac_counts[p[i]] == 0:
                ac_counts[p[i]] = 1
        else:
            penalties[p[i]] += 1
    ac_count = sum(ac_counts.values())
    penalty_count = sum([penalties[i] for i in penalties if ac_counts[i] == 1])
    print(ac_count, penalty_count)

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = [0]*M
    S = [0]*M
    for i in range(M):
        p[i], S[i] = input().split()
    main(N, M, p, S)
