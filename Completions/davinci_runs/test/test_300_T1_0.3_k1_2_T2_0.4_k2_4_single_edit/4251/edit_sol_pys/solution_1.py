
# Problem

# You are given an integer N. You need to print the series of all prime numbers till N.

# Input Format

# The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

# Output Format

# Print the desired output in single line separated by spaces.

# Constraints

# 1<=N<=1000

# Solution

def solve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n+1):
        if prime[p]:
            print(p, end=" ")

if __name__ == "__main__":
    n = int(input())
    solve(n)
