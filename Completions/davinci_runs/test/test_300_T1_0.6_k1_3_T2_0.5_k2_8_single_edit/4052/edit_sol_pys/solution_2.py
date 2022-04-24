

def solve(s, t):
    n = len(s)
    moves = []
    ans = []
    i = 0
    while i < n-1:
        if s[i] != t[i]:
            pos = s.find(t[i], i+1)
            moves.append(pos)
            ans.append(pos-i)
            s = swap(s, pos, pos-1)
        i += 1
    if s != t:
        return -1
    return len(moves), moves, ans

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
        moves, indices, ans = res
        print(moves)
        print(*indices)
        print(*ans)
