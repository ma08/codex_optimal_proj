
# D: number of problems
# G: total score
def main():
    D, G = map(int, input().split())
    # p: number of problems
    # c: bonus score
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    # calculate the minimum number of problems
    # that needs to be solved in order to have a total score of G or more points
    ans = float('inf')
    for i in range(2**D):
        score = 0
        res = 0  # number of problems that are solved
        for j in range(D):
            if (i>>j)&1:  # j-th bit is 1
                # score of problems that are solved
                score += 100 * (j+1) * p[j] + c[j]  # j+1: index of problem
                res += p[j]
        for j in range(D-1, -1, -1):
            if (i>>j)&1 == 0:  # j-th bit is 0
                # solve problems that are not solved
                for k in range(p[j]):
                    res += 1
                    score += 100 * (j+1)  # j+1: index of problem
                    if score >= G:
                        break
                break
        if score >= G:
            ans = min(ans, res)
    print(ans)

if __name__ == "__main__":
    main()
