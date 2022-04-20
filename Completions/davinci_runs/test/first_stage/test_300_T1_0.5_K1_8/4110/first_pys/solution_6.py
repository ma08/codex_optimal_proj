

def main():
    d, g = (int(i) for i in input().split())
    p, c = [], []
    for _ in range(d):
        p_i, c_i = (int(i) for i in input().split())
        p.append(p_i)
        c.append(c_i)
    ans = solve(d, g, p, c)
    print(ans)


def solve(d, g, p, c):
    ans = float('inf')
    for i in range(2**d):
        total_score, num_problems, rest_problems = 0, 0, []
        for j in range(d):
            if ((i >> j) & 1):
                total_score += (j+1)*100*p[j] + c[j]
                num_problems += p[j]
            else:
                rest_problems.append(j)
        if total_score < g:
            for j in reversed(rest_problems):
                need_problems = math.ceil((g-total_score)/((j+1)*100))
                if need_problems >= p[j]:
                    need_problems = p[j]
                total_score += need_problems*(j+1)*100
                num_problems += need_problems
                if total_score >= g:
                    break
        ans = min(ans, num_problems)
    return ans


if __name__ == '__main__':
    main()