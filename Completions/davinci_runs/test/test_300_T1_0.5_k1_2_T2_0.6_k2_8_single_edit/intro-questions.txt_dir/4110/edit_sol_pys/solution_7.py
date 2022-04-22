

def main():
    D, G = map(int, input().split())
    P, C = [], []
    for i in range(D):
        pi, ci = map(int, input().split())
        P.append(pi)
        C.append(ci)
    
    # calculate the minimum number of problems
    # that needs to be solved in order to have a total score of G or more points
    ans = float('inf')
    for i in range(2**D):
        score = 0
        res = 0
        for j in range(D):
            if (i>>j)&1:
                score += 100 * (j+1) * P[j] + C[j]
                res += P[j]
        for j in range(D-1, -1, -1):
            if (i>>j)&1 == 0:
                for k in range(P[j]):
                    res += 1
                    score += 100 * (j+1)
                    if score >= G:
                        break
                break
        if score >= G:
            ans = min(ans, res)
    print(ans)

if __name__ == "__main__":
    main()
