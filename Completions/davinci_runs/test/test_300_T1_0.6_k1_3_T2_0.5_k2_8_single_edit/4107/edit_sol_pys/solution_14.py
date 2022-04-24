

def solve(n, s):
    i = 0
    while i < n:
        if s[i] == '0':
            return i+1
        i += 1
    return i+1

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
