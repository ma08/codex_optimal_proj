

# python3
# Problem Statement: Given a string s consisting of n lowercase letters, you have to delete the minimum number of characters
# from s so that every letter in s becomes a distinct letter in the resulting string. We only care about the occurrences of
# each letter, not their positions in the original string.
#
# Input Format: The first line contains a single integer n, the length of s. The second line contains string s.
#
# Constraints: 1 <= n <= 10^5
#
# Output Format: Output the minimum number of characters that you have to delete to make the letters of the string s distinct.


from sys import stdin

def main():
    code = stdin.readline().strip()
    n = len(code)
    dp = [0] * (n + 4)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 0
    dp[3] = 0
    for i in range(4, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3], dp[i - 4]) + (1 if code[i - 1].isupper() else 0)
    print(dp[n])

if __name__ == '__main__':
    main()
