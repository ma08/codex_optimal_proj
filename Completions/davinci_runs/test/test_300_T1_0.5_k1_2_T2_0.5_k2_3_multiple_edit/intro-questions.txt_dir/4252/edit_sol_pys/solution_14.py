

# n = int(input())
# s = input()
# print("".join(s.split("xxx")))

def get_result(n, s):
    def find_next_xxx_index(string, start_index=0):
        index = start_index
        while index < len(string) and string[index] == "x":
            index += 1
        while index < len(string):
            if string[index] == "x":
                if string[index - 1] == "x" and string[index - 2] == "x":
                    return index
            index += 1
        return -1

    def remove_char_at_index(string, index):
        return string[:index] + string[index + 1:]

    def remove_first_xxx(string):
        i = find_next_xxx_index(string)
        if i == -1:
            return string
        return remove_char_at_index(string, i)

    result = len(s)
    while True:
        string = remove_first_xxx(s)
        result = min(result, len(string))
        i = find_next_xxx_index(s)
        if i == -1:
            return result
        string = remove_char_at_index(s, i)
        result = min(result, len(string))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
