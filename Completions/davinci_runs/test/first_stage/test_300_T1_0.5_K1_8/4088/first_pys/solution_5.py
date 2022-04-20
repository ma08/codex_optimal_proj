

def get_b(t):
    b = [0]*len(t)
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] < t[j]:
                b[i] += abs(i-j)
    return b

def get_t(s, b):
    t = [' ']*len(b)
    for i in range(len(b)):
        for j in range(len(s)):
            if b[i] == get_b(t[:i] + [s[j]] + t[i+1:])[i]:
                t[i] = s[j]
                s = s[:j] + s[j+1:]
                break
    return ''.join(t)

def main():
    q = int(input())
    for _ in range(q):
        s = input()
        m = int(input())
        b = [int(i) for i in input().split()]
        print(get_t(s, b))

if __name__ == '__main__':
    main()