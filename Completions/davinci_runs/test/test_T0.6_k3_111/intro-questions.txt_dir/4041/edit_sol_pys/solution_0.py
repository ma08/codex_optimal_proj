

def longestCommonSubstring(X, Y, m, n):
    L = [[0]*(n+1) for i in range(m+1)] # initialize 2d array
    for i in range(m+1): # iterate through array
        for j in range(n+1): # iterate through array
            if i == 0 or j == 0:
                L[i][j] = 0 # set to 0
            elif X[i-1] == Y[j-1]: # if the characters are the same
                L[i][j] = L[i-1][j-1] + 1 # add 1 to the previous count
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1]) # set to max of previous count
    return L[m][n] # return the count

def main():
    X = list(input()) # get input
    Y = list(input()) # get input
    m = len(X) # get length of X
    n = len(Y) # get length of Y
    print(m - longestCommonSubstring(X, Y, m, n)) # print the difference

main() # call main
