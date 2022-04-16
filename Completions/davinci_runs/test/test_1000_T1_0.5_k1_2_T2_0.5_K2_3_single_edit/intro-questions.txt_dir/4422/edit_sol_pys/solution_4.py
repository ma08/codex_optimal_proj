

def string_case(n, k, s, p):
    return s[:k-1] + s[k-1].lower() + s[k:] + p


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    p = input()
    print(string_case(n, k, s, p))
