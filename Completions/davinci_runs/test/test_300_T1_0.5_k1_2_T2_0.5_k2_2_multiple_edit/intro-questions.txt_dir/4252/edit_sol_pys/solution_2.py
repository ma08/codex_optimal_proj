

def get_result(n, s):
    def find_next_xxx_index(s, start_index=0):
        index = start_index
        while index < len(s) and s[index] == "x":
            index += 1
        while index < len(s) - 2:
            if s[index] == "x":
                if s[index - 1] == "x" and s[index - 2] == "x":
                    return index
            index += 1
        return -1

        return -1

    def remove_xxx_at_index(s, index):
        if index == -1:
            return s, -1
        return s[:index] + s[index + 3:], index

    result = len(s)
    while True:
        s, i = remove_xxx_at_index(s, find_next_xxx_index(s))
        result = min(result, len(s))
        if find_next_xxx_index(s) == -1:
            return result
        s, i = remove_xxx_at_index(s, i)
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
