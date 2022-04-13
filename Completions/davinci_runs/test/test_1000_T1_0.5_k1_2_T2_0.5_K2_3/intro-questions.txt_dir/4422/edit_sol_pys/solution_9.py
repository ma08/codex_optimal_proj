

def string_case(k, s):
    return s[:k-1] + s[k-1].lower() + s[k:]


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(string_case(k, s))
