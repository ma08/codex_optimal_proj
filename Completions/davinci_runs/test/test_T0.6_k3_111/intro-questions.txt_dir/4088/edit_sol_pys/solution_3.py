
import sys


def solve(s, b):
    pos = []
    for i in range(len(s)):
        pos.append([s[i], b[i], i+1])
    pos = sorted(pos)
    res = ""
    start = 0
    end = len(s) - 1
    for i in range(len(s)):
        if pos[i][1] == 0:
            res += pos[i][0]
            continue
        if i == 0:
            res += pos[i][0]
            start = pos[i][2]
            continue
        if i == len(s) - 1:
            res += pos[i][0]
            end = pos[i][2]
            continue
        if pos[i][1] > pos[i-1][1]:
            res += pos[i][0]
            start = pos[i][2]
            continue
        if pos[i][1] < pos[i-1][1]:
            res += pos[i][0]
            end = pos[i][2]
            continue
        if pos[i][1] == pos[i-1][1]:
            if pos[i][2] < start:
                res += pos[i][0]
                start = pos[i][2]
            elif pos[i][2] > end:
                res += pos[i][0]
                end = pos[i][2]
            else:
                res += pos[i][0]
    return res


if __name__ == "__main__":
    q = int(input())
    ans = []
    for i in range(q):
        s = input()
        m = int(input())
        b = list(map(int, input().split()))
        ans.append(solve(s, b))
    for i in range(q):
        print(ans[i])
