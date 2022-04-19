

import sys

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    s2_dict = {}
    for c in s1:
        if c not in s1_dict:
            s1_dict[c] = 1
        else:
            s1_dict[c] += 1
    for c in s2:
        if c not in s2_dict:
            s2_dict[c] = 1
        else:
            s2_dict[c] += 1
    return s1_dict == s2_dict

def main():
    n = int(sys.stdin.readline().rstrip())
    s = []
    for _ in range(n):
        s.append(sys.stdin.readline().rstrip())
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if is_anagram(s[i], s[j]):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
