

def solve(s, t):
    n = len(s)
    moves = 0
    ans = []
    for i in range(n-1, -1, -1):
        if s[i] != t[i]:
            pos = s.rfind(t[i])
            ans.append(pos)
            moves += 1
            s = swap(s, pos, i)
    if s != t:
        return -1
    return moves, ans[::-1]

def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()
    res = solve(s, t)
    if res == -1:
        print(-1)
    else:
        moves, ans = res
        print(moves)
        print(*ans)
