

def get_result(n, s):
    result = len(s)
    for i in range(n):
        if i < n - 2 and s[i] == "x" and s[i + 1] == "x" and s[i + 2] == "x":
            result = min(result, get_result(n - 1, s[:i] + s[i + 1:]))
    return result

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_result(n, s))
