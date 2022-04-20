
import sys

def is_anagram(s1, s2):
    s1_dict = {}
    s2_dict = {}
    for c1, c2 in zip(s1, s2):
        s1_dict[c1] = s1_dict.get(c1, 0) + 1
        s2_dict[c2] = s2_dict.get(c2, 0) + 1
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
