

# n = int(input())
# s = input()
# print("".join(s.split("xxx")))  # This is a wrong solution

def get_result(n, s):
    def find_next_xxx_index(start_index=0):
        index = start_index
        while index < len(s) and s[index] == "x":
            index += 1
        while index < len(s):
            if s[index] == "x":
                if s[index - 1] == "x" and s[index - 2] == "x":
                    return index
            index += 1
        return -1

    def remove_char_at_index(index):
        return s[:index] + s[index + 1:]

    def remove_first_xxx():
        i = find_next_xxx_index()
        if i == -1:
            return
        return remove_char_at_index(i)

    result = len(s)
    while True:
        remove_first_xxx()
        result = min(result, len(s))
        i = find_next_xxx_index()
        if i == -1:
            return result
        remove_char_at_index(i)
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
