

def f(n, s, m):
	dp = [0 for i in range(m+1)]
	dp[0] = 1
	for i in range(len(s)):
		if(s[i]=='('):
			for j in range(i+1, m+1):
				dp[j]+=dp[j-1]
				dp[j]%=1000000007 
		else:
			for j in range(i+1, m+1):
				dp[j]+=dp[j-1]
				dp[j]%=1000000007
	return dp[m]

n = int(input())
s = input()
print(f(n, s, 2*n))
