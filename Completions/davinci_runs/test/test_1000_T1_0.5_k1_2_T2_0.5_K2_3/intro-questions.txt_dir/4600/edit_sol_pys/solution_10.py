from collections import defaultdict

def main(N, M, p, S):
    ac_count = defaultdict(int)
    penalties = defaultdict(int)
    for i in range(M):
        if S[i] == 'AC':
            if ac_count[p[i]] == 0:
                ac_count[p[i]] = 1
        else:
            penalties[p[i]] += 1
    ac_num = sum(ac_count.values())
    penalty_num = sum([penalties[i] for i in penalties if ac_count[i] == 1])
    print(ac_num, penalty_num)

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = [0]*M
    S = [0]*M
    for i in range(M):
        p[i], S[i] = input().split()
    main(N, M, p, S)
