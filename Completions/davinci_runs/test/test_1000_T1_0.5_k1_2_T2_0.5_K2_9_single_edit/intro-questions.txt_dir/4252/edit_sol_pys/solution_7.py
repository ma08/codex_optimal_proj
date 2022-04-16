

def get_result(n, s):
    result = len(s)
    for i in range(n):
        if s[i] == "x":
            if i + 2 < n and s[i + 1] == "x" and s[i + 2] == "x":
                result = min(result, len(s[:i] + s[i + 1:]))

    return result


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
