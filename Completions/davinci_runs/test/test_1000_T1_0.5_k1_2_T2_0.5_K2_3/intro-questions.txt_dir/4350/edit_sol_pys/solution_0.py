

#--------------------------------------------------------------------------------#
def main():
    n,m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    #print(arr)
    #print(n,m)
    ans = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                #print(i,j)
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
    #print(arr)
    if any('*' in sublist for sublist in arr): # any function checks if any element in arr is *
        print(-1)
    else:
        print(len(ans))
        for i in ans:
            print(*i)

main()
