

def main():
    D, G = map(int, input().split())
    p, c = [], [] # p[i]: score, c[i]: bonus
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    
    # calculate the minimum number of problems
    # that needs to be solved in order to have a total score of G or more points
    ans = float('inf')
    for i in range(2**D):
        score = 0
        res = 0 # number of problems solved
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j+1) * p[j] + c[j]
                res += p[j]
        for j in range(D-1, -1, -1):
            if (i >> j) & 1 == 0:
                for k in range(p[j]):
                    res += 1
                    score += 100 * (j+1)
                    if score >= G: break
                break # for k
        if score >= G:
            ans = min(ans, res)
    print(ans)

if __name__ == "__main__":
    main()
