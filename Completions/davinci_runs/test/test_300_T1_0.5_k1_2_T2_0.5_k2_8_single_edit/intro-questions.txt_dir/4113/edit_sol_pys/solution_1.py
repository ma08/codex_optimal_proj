
N = int(input())

def dfs(i, j):
    if i == N:
        return True

    if j == 4:
        if dfs(i+7, 0):
            return True
    else:
        if dfs(i+4, j+1):
            return True

    return False

if dfs(0, 0):
    print("Yes")
else:
    print("No")
