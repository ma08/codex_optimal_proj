

import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(len(s) - lcs(s, t))

def lcs(s, t):
    """
    Returns the length of the longest common subsequence of s and t
    """
    # Build a matrix of length s and t
    m = [[0 for _ in range(len(t))] for _ in range(len(s))]
    # Fill in the first row and column
    for i in range(len(s)):
        if s[i] == t[0]:
            m[i][0] = 1
        elif i != 0:
            m[i][0] = m[i-1][0]
    for j in range(len(t)):
        if t[j] == s[0]:
            m[0][j] = 1
        elif j != 0:
            m[0][j] = m[0][j-1]
    # Fill in the rest of the matrix
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                m[i][j] = m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])
    return m[len(s)-1][len(t)-1]

if __name__ == "__main__":
    main()
