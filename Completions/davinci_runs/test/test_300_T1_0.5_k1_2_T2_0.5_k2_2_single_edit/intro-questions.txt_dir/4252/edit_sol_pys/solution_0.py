

# n = int(input())
# s = input()
# print("".join(s.split("xxx")))

def get_result(n, s):
    def remove_first_xxx(s):
        def find_next_xxx_index(s, start_index=0):
            index = start_index
            while index < len(s) and s[index] == "x":
                index += 1
            while index < len(s):
                if s[index] == "x":
                    if s[index - 1] == "x" and s[index - 2] == "x":
                        return index
                index += 1
            return -1

        def remove_char_at_index(s, index):
            return s[:index] + s[index + 1:]

        i = find_next_xxx_index(s)
        if i == -1:
            return s
        return remove_char_at_index(s, i)

    result = len(s)
    while True:
        if result == 0:
            return 0
        else:
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
