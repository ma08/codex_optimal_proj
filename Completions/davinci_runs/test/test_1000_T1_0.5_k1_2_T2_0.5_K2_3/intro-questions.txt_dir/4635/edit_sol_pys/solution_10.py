
import random
import string

def random_string(n):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(n)])

def generate_random_testcase(n, k):
    return ''.join([random.choice(string.ascii_lowercase[:k]) for _ in range(n)])

def generate_testcases(t):
    testcases = []
    for _ in range(t):
        n = random.randint(1, 100)
        k = random.randint(1, 26)
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
    if set(s) == 1:
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
