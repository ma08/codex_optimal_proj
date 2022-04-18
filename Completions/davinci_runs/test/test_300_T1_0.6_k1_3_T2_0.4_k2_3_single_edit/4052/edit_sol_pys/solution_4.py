

def solve(s, t):
    n = len(s)
    moves = 0
    ans = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        else:
            pos = s[i:].find(t[i])
            if pos == -1:
                return -1
            else:
                while pos != 0:
                    ans.append(pos+i)
                    moves += 1
                    s = swap(s, pos+i, pos+i-1)
                    pos = s[i:].find(t[i])
    if s != t:
        return -1
    return moves, ans

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
        for i in ans:
            print(i, end=' ')
        print()
