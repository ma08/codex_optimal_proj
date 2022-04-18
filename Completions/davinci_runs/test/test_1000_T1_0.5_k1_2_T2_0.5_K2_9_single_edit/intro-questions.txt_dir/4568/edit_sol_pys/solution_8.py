


def solve(s):
    return len(set(s[:len(s)//2]) & set(s[len(s)//2:]))

if __name__ == '__main__':
    print(solve(input()))
