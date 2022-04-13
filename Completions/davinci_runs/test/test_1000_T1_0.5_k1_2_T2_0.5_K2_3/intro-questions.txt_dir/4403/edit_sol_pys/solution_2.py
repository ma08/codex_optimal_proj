
import sys

sys.setrecursionlimit(10 ** 7)

S = input()  # input


def dfs(i, count):
    if i == len(S):
        ans.append(count)
        return

    if S[i] == "+":
        dfs(i + 1, count + 1)
    else:
        dfs(i + 1, count - 1)


ans = []
dfs(0, 0)
print(ans)
