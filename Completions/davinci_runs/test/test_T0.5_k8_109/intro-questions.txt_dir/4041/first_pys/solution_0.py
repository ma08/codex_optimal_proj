

import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    s_i = 0
    t_i = 0
    res = 0
    while s_i < len(s) and t_i < len(t):
        if s[s_i] == t[t_i]:
            s_i += 1
            t_i += 1
        else:
            res += 1
            s_i += 1
    res += len(s) - s_i
    print(res)

if __name__ == "__main__":
    main()