# for i in range(int(input())):
#     n,m = map(int,input().split())
#     grid = []
#     for j in range(n):
#         grid.append(list(input()))
#     stars = []
#     for j in range(n):
#         for k in range(m):
#             if (grid[j][k] == '*'):
#                 if (j>0 and k>0 and grid[j-1][k-1] == '*') or (j>0 and grid[j-1][k] == '*') or (j>0 and k<m-1 and grid[j-1][k+1] == '*') or (k>0 and grid[j][k-1] == '*') or (k<m-1 and grid[j][k+1] == '*') or (j<n-1 and k>0 and grid[j+1][k-1] == '*') or (j<n-1 and grid[j+1][k] == '*') or (j<n-1 and k<m-1 and grid[j+1][k+1] == '*'):
#                     stars.append([j+1,k+1,1])
#                 else:
#                     flag = True
#                     r = 0
#                     while(flag):
#                         r += 1
#                         if (j-r<0 or k-r<0 or j+r>=n or k+r>=m):
#                             flag = False
#                         else:
#                             if (grid[j-r][k-r] == '*' and grid[j-r][k+r] == '*' and grid[j+r][k-r] == '*' and grid[j+r][k+r] == '*'):
#                                 stars.append([j+1,k+1,r+1])
#                             else:
#                                 flag = False
#     if (len(stars) == 0):
#         print("-1")
#     else:
#         print(len(stars))
#         for j in range(len(stars)):
#             print(stars[j][0],stars[j][1],stars[j][2])

n,m = map(int,input().split())

grid = []
for i in range(n):

    grid.append(list(input()))

stars = []
for i in range(n):

    for j in range(m):
        if (grid[i][j] == '*'):

            if (i>0 and j>0 and grid[i-1][j-1] == '*') or (i>0 and grid[i-1][j] == '*') or (i>0 and j<m-1 and grid[i-1][j+1] == '*') or (j>0 and grid[i][j-1] == '*') or (j<m-1 and grid[i][j+1] == '*') or (i<n-1 and j>0 and grid[i+1][j-1] == '*') or (i<n-1 and grid[i+1][j] == '*') or (i<n-1 and j<m-1 and grid[i+1][j+1] == '*'):

                stars.append([i+1,j+1,1])

            else:

                flag = True

                r = 0

                while(flag):

                    r += 1

                    if (i-r<0 or j-r<0 or i+r>=n or j+r>=m):

                        flag = False

                    else:

                        if (grid[i-r][j-r] == '*' and grid[i-r][j+r] == '*' and grid[i+r][j-r] == '*' and grid[i+r][j+r] == '*'):

                            stars.append([i+1,j+1,r+1])

                        else:

                            flag = False

if (len(stars) == 0):

    print("-1")

else:

    print(len(stars))

    for i in range(len(stars)):

        print(stars[i][0],stars[i][1],stars[i][2])
