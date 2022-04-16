

    if "xxx" not in s:
        return n
def get_result(n, s):
    def find_next_xxx_index(s, start_index=0):
        index = start_index
        while index < len(s) and s[index] == 'x':
            index += 1
        while index < len(s):
            if s[index] == 'x':
                if s[index - 1] == 'x' and s[index - 2] == 'x':
                    return index
            index += 1
        return -1

    result = len(s)
    while True:
        i = find_next_xxx_index(s)
        if i == -1:
            return result
        s = s[:i] + s[i + 1:]
        result = min(result, len(s))
        i = find_next_xxx_index(s)
        if i == -1:
            return result
        s = s[:i] + s[i + 1:]
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
