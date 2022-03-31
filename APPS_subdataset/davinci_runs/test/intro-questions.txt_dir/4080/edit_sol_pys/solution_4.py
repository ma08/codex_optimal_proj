
import random

def gen_random_array(n, m):
    a = []
    for i in range(n):
        a.append(random.randint(-m, m))
    return a

def gen_random_segments(n, m):
    s = []
    for i in range(m):
        l = random.randint(1, n)
        r = random.randint(l, n)
        s.append([l, r])
    return s

def gen_random_subset(m):
    s = set()
    while True:
        s.add(random.randint(1, m))
        if len(s) == m:
            break
    return list(s)

def brute_force(a, s, m):
    d = 0
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            for k in range(j+1, m+1):
                for l in range(k+1, m+1):
                    b = [x for x in a]
                    b[s[i-1][0]-1:s[i-1][1]] = [x-1 for x in b[s[i-1][0]-1:s[i-1][1]]]
                    b[s[j-1][0]-1:s[j-1][1]] = [x-1 for x in b[s[j-1][0]-1:s[j-1][1]]]
                    b[s[k-1][0]-1:s[k-1][1]] = [x-1 for x in b[s[k-1][0]-1:s[k-1][1]]]
                    b[s[l-1][0]-1:s[l-1][1]] = [x-1 for x in b[s[l-1][0]-1:s[l-1][1]]]
                    if max(b) - min(b) > d:
                        d = max(b) - min(b)
    return d

def solve(a, s, m):
    d = 0
    s_i = []
    for i in range(m):
        if (s[i][1] - s[i][0]) % 2 == 0:
            b = [x for x in a]
            b[s[i][0]-1:s[i][1]] = [x-1 for x in b[s[i][0]-1:s[i][1]]]
            if max(b) - min(b) > d:
                d = max(b) - min(b)
                s_i = [i+1]
        else:
            b = [x for x in a]
            b[s[i][0]-1:s[i][1]] = [x-1 for x in b[s[i][0]-1:s[i][1]]]
            if max(b) - min(b) > d:
                d = max(b) - min(b)
                s_i = [i+1]
            b = [x for x in a]
            b[s[i][0]-1:s[i][1]] = [x-2 for x in b[s[i][0]-1:s[i][1]]]
            if max(b) - min(b) > d:
                d = max(b) - min(b)
                s_i = [i+1]
    return d, s_i

def main():
    n = random.randint(1, 10**4)
    m = random.randint(1, 10**4)
    a = gen_random_array(n, 10**5)
    s = gen_random_segments(n, m)
    print(n, m)
    print(' '.join([str(x) for x in a]))
    for i in range(m):
        print(s[i][0], s[i][1])
    d, s_i = solve(a, s, m)
    print(d)
    print(len(s_i))
    print(' '.join([str(x) for x in s_i]))

if __name__ == '__main__':
    main()
