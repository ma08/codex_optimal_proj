

import sys

def main():
    S = sys.stdin.readline().rstrip()
    max_len = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if is_ACGT(S[i:j+1]):
                if max_len < j - i + 1:
                    max_len = j - i + 1
    print(max_len)

def is_ACGT(s):
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    main()