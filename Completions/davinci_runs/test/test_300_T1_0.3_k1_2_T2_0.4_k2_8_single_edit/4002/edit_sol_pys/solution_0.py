
def main():n,m,k=map(int,input().split());a=[];for i in range(n):a.append(list(map(int,input().split())));dp=[[0]*(k+1)for i in range(m+1)];for i in range(n):for j in range(m):for x in range(k):dp[j+1][(x+a[i][j])%k]=max(dp[j+1][(x+a[i][j])%k],dp[j][x]+a[i][j]);print(dp[m][0])
main() 
