
import sys

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()
    return s1_list == s2_list


def main():
    n = int(sys.stdin.readline().rstrip())
    s = []
    for _ in range(n):
        s.append(sys.stdin.readline().rstrip())
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(s[i], s[j]):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
