

n,m=[int(i) for i in input().split()]
mat=[]
for i in range(n):
    mat.append([int(j) for j in input().split()])

def check(mat):
    for i in range(n):
        for j in range(m-1):
            if mat[i][j]>mat[i][j+1]:
                return False
    return True

def row(mat,n):
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                mat[i][j]=0
            else:
                mat[i][j]=1
    return mat

def col(mat,m):
    for i in range(n):
        for j in range(m):
            if mat[j][i]==1:
                mat[j][i]=0
            else:
                mat[j][i]=1
    return mat

def solve(mat,n,m):
    for i in range(n):
        if mat[i][0]==1:
            mat=row(mat,i)
    for i in range(m):
        if mat[0][i]==1:
            mat=col(mat,i)
    return mat

if check(mat):
    print("YES")
    mat=solve(mat,n,m)
    ans_row=""
    ans_col=""
    for i in range(n):
        if mat[i][0]==1:
            ans_row+="1"
        else:
            ans_row+="0"
    for i in range(m):
        if mat[0][i]==1:
            ans_col+="1"
        else:
            ans_col+="0"
    print(ans_row)
    print(ans_col)
else:
    print("NO")