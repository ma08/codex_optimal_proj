

import string

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    for c in string.ascii_lowercase:
        if s1.count(c) != s2.count(c):
            return False
    return True

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if anagram(s[i], s[j]):
                count += 1
    print(count)

if __name__ == '__main__':
    main()