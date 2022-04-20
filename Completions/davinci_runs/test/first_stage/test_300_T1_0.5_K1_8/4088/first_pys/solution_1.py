

from random import randint
from random import shuffle

def generate_string(m):
    return ''.join([chr(randint(ord('a'), ord('z'))) for i in range(m)])

def generate_b(s):
    b = [0 for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                b[i] += abs(i - j)
    return b

def get_result(s, b):
    n = len(s)
    t = ['' for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (b[j] == 0):
                t[j] = s[i]
                b[j] = -1
                break
            else:
                b[j] -= abs(j - i)
    return ''.join(t)

def main():
    q = randint(1, 100)
    print(q)
    for i in range(q):
        m = randint(1, 50)
        s = generate_string(m)
        b = generate_b(s)
        shuffle(b)
        print(s)
        print(len(b))
        print(' '.join([str(x) for x in b]))

if __name__ == '__main__':
    main()