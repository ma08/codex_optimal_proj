


def main():
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    ans = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                k = 1
                while i+k < n and i-k >= 0 and j+k < m and j-k >= 0:
                    if arr[i+k][j] == '*' and arr[i-k][j] == '*' and arr[i][j+k] == '*' and arr[i][j-k] == '*':
                        for l in range(1,k+1):
                            arr[i+l][j] = '.'
                            arr[i-l][j] = '.'
                            arr[i][j+l] = '.'
                            arr[i][j-l] = '.'
                        ans.append([i+1,j+1,k])
                    k += 1
    if any('*' in sublist for sublist in arr):
        print(-1)
    else:
        print(len(ans))
        for i in ans:
            print(*i)

main()
