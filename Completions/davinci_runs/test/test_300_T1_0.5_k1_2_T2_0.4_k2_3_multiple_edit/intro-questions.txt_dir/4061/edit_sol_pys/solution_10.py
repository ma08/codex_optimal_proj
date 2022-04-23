


import sys

def main():
    """
    We can note that for each character in s, we can either keep it or remove it.
    We can keep it if it is in t. 
    We can remove it if it is not in t (or if we have already removed it). 
    This leads to a simple dp solution. 
    We keep a list of the length of the longest possible substring we can remove ending at each index in s.
    """
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    n = len(s)
    dp = [0] * n
    for i in range(n):
        if s[i] in t:
            if i == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
        else:
            if i == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1
    print(max(dp))

if __name__ == "__main__":
    main()
