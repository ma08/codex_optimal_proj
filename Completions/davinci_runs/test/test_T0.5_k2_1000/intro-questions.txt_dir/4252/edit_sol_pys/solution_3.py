

# n = int(input())
# s = input()
# print("".join(s.split("xxx")))  # this is wrong, it will remove all xxx, not just the first one

def get_result(n, s):
    def find_next_xxx_index(s, start_index=0):
        index = start_index
        while index < len(s) and s[index] == "x":  # skip all x at the beginning
            index += 1
        while index < len(s):
            if s[index] == "x":  # find the first x
                if s[index - 1] == "x" and s[index - 2] == "x":
                    return index
            index += 1
        return -1  # not found

    def remove_char_at_index(s, index):
        return s[:index] + s[index + 1:]  # remove the char at index

    def remove_first_xxx(s):
        i = find_next_xxx_index(s)  # find the first xxx
        if i == -1:  # not found
            return s
        return remove_char_at_index(s, i)

    result = len(s)
    while True:
        s = remove_first_xxx(s)  # remove the first xxx
        result = min(result, len(s))
        i = find_next_xxx_index(s)  # find the first xxx
        if i == -1:  # not found
            return result
        s = remove_char_at_index(s, i)  # remove the first x
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
