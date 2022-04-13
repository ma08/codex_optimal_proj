

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
        return random_string(n // 2) + 'b' * (n - n // 2)
    if k == 3:
        return random_string(n // 3) + 'b' * (n - n // 3) + 'c' * (n - n // 3)
    if k == 4:
        return random_string(n // 4) + 'b' * (n - n // 4) + 'c' * (n - n // 4) + 'd' * (n - n // 4)
    if k == 5:
        return random_string(n // 5) + 'b' * (n - n // 5) + 'c' * (n - n // 5) + 'd' * (n - n // 5) + 'e' * (n - n // 5)
    if k == 6:
        return random_string(n // 5) + 'b' * (n - n // 5) + 'c' * (n - n // 5) + 'd' * (n - n // 5) + 'e' * (n - n // 5)
    if k == 7:
        return random_string(n // 6) + 'b' * (n - n // 6) + 'c' * (n - n // 6) + 'd' * (n - n // 6) + 'e' * (n - n // 6) + 'f' * (n - n // 6)
    if k == 8:
        return random_string(n // 6) + 'b' * (n - n // 6) + 'c' * (n - n // 6) + 'd' * (n - n // 6) + 'e' * (n - n // 6) + 'f' * (n - n // 6) + 'g' * (n - n // 6)
    if k == 9:
        return random_string(n // 7) + 'b' * (n - n // 7) + 'c' * (n - n // 7) + 'd' * (n - n // 7) + 'e' * (n - n // 7) + 'f' * (n - n // 7) + 'g' * (n - n // 7)
    if k == 10:
        return random_string(n // 8) + 'b' * (n - n // 8) + 'c' * (n - n // 8) + 'd' * (n - n // 8) + 'e' * (n - n // 8) + 'f' * (n - n // 8) + 'g' * (n - n // 8) + 'h' * (n - n // 8)
    if k == 11:
        return random_string(n // 9) + 'b' * (n - n // 9) + 'c' * (n - n // 9) + 'd' * (n - n // 9) + 'e' * (n - n // 9) + 'f' * (n - n // 9) + 'g' * (n - n // 9) + 'h' * (n - n // 9) + 'i' * (n - n // 9)
    if k == 12:
        return random_string(n // 9) + 'b' * (n - n // 9) + 'c' * (n - n // 9) + 'd' * (n - n // 9) + 'e' * (n - n // 9) + 'f' * (n - n // 9) + 'g' * (n - n // 9) + 'h' * (n - n // 9) + 'i' * (n - n // 9)
    if k == 13:
        return random_string(n // 10) + 'b' * (n - n // 10) + 'c' * (n - n // 10) + 'd' * (n - n // 10) + 'e' * (n - n // 10) + 'f' * (n - n // 10) + 'g' * (n - n // 10) + 'h' * (n - n // 10) + 'i' * (n - n // 10) + 'j' * (n - n // 10)
    if k == 14:
        return random_string(n // 10) + 'b' * (n - n // 10) + 'c' * (n - n // 10) + 'd' * (n - n // 10) + 'e' * (n - n // 10) + 'f' * (n - n // 10) + 'g' * (n - n // 10) + 'h' * (n - n // 10) + 'i' * (n - n // 10) + 'j' * (n - n // 10) + 'k' * (n - n // 10)
    if k == 15:
        return random_string(n // 11) + 'b' * (n - n // 11) + 'c' * (n - n // 11) + 'd' * (n - n // 11) + 'e' * (n - n // 11) + 'f' * (n - n // 11) + 'g' * (n - n // 11) + 'h' * (n - n // 11) + 'i' * (n - n // 11) + 'j' * (n - n // 11) + 'k' * (n - n // 11)
    if k == 16:
        return random_string(n // 12) + 'b' * (n - n // 12) + 'c' * (n - n // 12) + 'd' * (n - n // 12) + 'e' * (n - n // 12) + 'f' * (n - n // 12) + 'g' * (n - n // 12) + 'h' * (n - n // 12) + 'i' * (n - n // 12) + 'j' * (n - n // 12) + 'k' * (n - n // 12) + 'l' * (n - n // 12)
    if k == 17:
        return random_string(n)
    if k == 18:
        return random_string(n)
    if k == 19:
        return random_string(n)
    if k == 20:
        return random_string(n)
    if k == 21:
        return random_string(n)
    if k == 22:
        return random_string(n)
    if k == 23:
        return random_string(n)
    if k == 24:
        return random_string(n)
    if k == 25:
        return random_string(n)

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
