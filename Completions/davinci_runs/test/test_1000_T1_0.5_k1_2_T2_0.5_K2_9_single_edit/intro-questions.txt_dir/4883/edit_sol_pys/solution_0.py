
import sys

def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())  # m is num of rules, n is num of test cases
    d = dict()
    for _ in range(m):
        a, b = input().split()
        d[a] = b
    for _ in range(n):
        a, b = input().split()
        if len(a) != len(b):  # if length of a and b are not equal, print no
            print('no')
            continue
        flag = True
        for i in range(len(a)):  # check if a and b are equal after applying rules
            if a[i] not in d or b[i] not in d or d[a[i]] != b[i]:
                flag = False
                break
        if flag:
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    main()
