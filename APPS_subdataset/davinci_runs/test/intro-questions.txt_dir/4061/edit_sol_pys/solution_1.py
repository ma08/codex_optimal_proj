
import sys

def lcs(s, t):
    l = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                l[i+1][j+1] = l[i][j] + 1
            else:
                l[i+1][j+1] = max(l[i+1][j], l[i][j+1])
    return l[-1][-1]


def main():
    # read in the data.
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    # the answer is the length of s minus the length of the longest common subsequence of s and t.
    print len(s) - lcs(s, t)


if __name__ == '__main__':
    main()
