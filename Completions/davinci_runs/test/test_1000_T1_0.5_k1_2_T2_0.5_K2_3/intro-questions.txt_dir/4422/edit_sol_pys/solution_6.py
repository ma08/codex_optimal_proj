

def string_case(s, k):
    return s[:k-1] + s[k-1].upper() + s[k:]


if __name__ == '__main__':
    k = int(input())
    s = input()
    print(string_case(s, k))
