
import random
import string

def random_string(n):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(n)])

def generate_random_testcase(n, k):
    if k == 1:
        return 'a' * n
    if k == 2:
        return random_string(n)
    if k == 3:
        return random_string(n)
    if k == 4:
        return random_string(n)
    if k == 5:
        return random_string(n)
    if k == 6:
        return random_string(n)
    if k == 7:
        return random_string(n)
    if k == 8:
        return random_string(n)
    if k == 9:
        return random_string(n)
    if k == 10:
        return random_string(n)
    if k == 11:
        return random_string(n)
    if k == 12:
        return random_string(n)
    if k == 13:
        return random_string(n)
    if k == 14:
        return random_string(n)
    if k == 15:
        return random_string(n)
    if k == 16:
        return random_string(n)
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
