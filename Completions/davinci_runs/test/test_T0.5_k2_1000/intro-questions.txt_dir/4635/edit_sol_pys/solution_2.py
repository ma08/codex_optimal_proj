
import random

import string

def random_string(n):

    return ''.join([random.choice(string.ascii_lowercase) for _ in range(n)])

def generate_random_testcase(n, k):
    if k == 26:
        return random_string(n)
    if k == 1:
        return 'a' * n
    if k == 2:
        return random_string(n // 2) * 2
    if k == 3:
        return random_string(n // 3) * 3
    if k == 4:
        return random_string(n // 4) * 4
    if k == 5:
        return random_string(n // 5) * 5
    if k == 6:
        return random_string(n // 6) * 6
    if k == 7:
        return random_string(n // 7) * 7
    if k == 8:
        return random_string(n // 8) * 8
    if k == 9:
        return random_string(n // 9) * 9
    if k == 10:
        return random_string(n // 10) * 10
    if k == 11:
        return random_string(n // 11) * 11
    if k == 12:
        return random_string(n // 12) * 12
    if k == 13:
        return random_string(n // 13) * 13
    if k == 14:
        return random_string(n // 14) * 14
    if k == 15:
        return random_string(n // 15) * 15
    if k == 16:
        return random_string(n // 16) * 16
    if k == 17:
        return random_string(n // 17) * 17
    if k == 18:
        return random_string(n // 18) * 18
    if k == 19:
        return random_string(n // 19) * 19
    if k == 20:
        return random_string(n // 20) * 20
    if k == 21:
        return random_string(n // 21) * 21
    if k == 22:
        return random_string(n // 22) * 22
    if k == 23:
        return random_string(n // 23) * 23
    if k == 24:
        return random_string(n // 24) * 24
    if k == 25:
        return random_string(n // 25) * 25


def generate_testcases(t):
    testcases = []
    for _ in range(t):
        n = random.randint(1, 100)
        k = random.randint(1, min(n, 26))
        testcases.append(generate_random_testcase(n, k))
    return testcases


def write_testcases(testcases, filename='testcases.txt'):
    with open(filename, 'w') as f:
        f.write(str(len(testcases)) + '\n')
        for testcase in testcases:
            f.write(testcase + '\n')


def check(s):
    if len(s) == 1:
        return True
    if len(set(s)) == 1:
        return False
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


def check_testcases(filename='testcases.txt'):
    with open(filename, 'r') as f:
        t = int(f.readline())
        testcases = []
        for _ in range(t):
            n, k = map(int, f.readline().split())
            testcases.append((n, k))
    for testcase in testcases:
        if not check(generate_random_testcase(*testcase)):
            print(testcase)


if __name__ == '__main__':
    check_testcases()
