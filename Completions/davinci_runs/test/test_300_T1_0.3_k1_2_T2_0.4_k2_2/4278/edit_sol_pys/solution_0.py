
import sys

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


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
