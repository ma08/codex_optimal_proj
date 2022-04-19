

# n = int(input())
# s = input()
# print("".join(s.split("xxx")))

def get_result(n, s):
    def find_next_xxx_index(s, start_index=0):  # s -> string, start_index -> int
        index = start_index  # index -> int
        while index < len(s) and s[index] == "x":  # s[index] -> string
            index += 1  # index -> int
        while index < len(s):  # s[index] -> string
            if s[index] == "x" and s[index - 1] == "x" and s[index - 2] == "x":
                return index
            index += 1  # index -> int
        return -1  # index -> int

    def remove_char_at_index(s, index):
        return s[:index] + s[index + 1:]

    def remove_first_xxx(s):
        i = find_next_xxx_index(s)
        if i == -1:
            return s
        return remove_char_at_index(s, i)

    result = len(s)
    while True:
        s = remove_first_xxx(s)
        result = min(result, len(s))
        i = find_next_xxx_index(s)
        if i == -1:
            return result
        s = remove_char_at_index(s, i)
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
