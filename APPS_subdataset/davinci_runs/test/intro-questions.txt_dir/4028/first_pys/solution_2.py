

def main():
    n = int(input())
    s = input()
    print(solve(n, s))

def solve(n, s):
    num_ways = [1,1]
    for i in range(2,2*n+1):
        num_ways.append(num_ways[i-1]+num_ways[i-2])
    if s[0] == '(':
        s_left_parens = 1
    else:
        s_left_parens = 0
    s_right_parens = len(s) - s_left_parens
    if s_left_parens > s_right_parens:
        return 0
    if s_left_parens > n:
        return 0
    if s_right_parens > n:
        return 0
    if s_left_parens == s_right_parens:
        return num_ways[s_left_parens]
    if s_left_parens == n:
        return num_ways[s_right_parens]
    if s_right_parens == n:
        return num_ways[s_left_parens]
    return (num_ways[s_left_parens] * num_ways[s_right_parens]) % (10**9+7)

if __name__ == "__main__":
    main()