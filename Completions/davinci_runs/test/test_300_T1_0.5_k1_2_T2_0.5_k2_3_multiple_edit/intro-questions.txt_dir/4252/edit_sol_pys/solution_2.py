

def get_result(n, s):
    def find_next_xxx_index(s):
        index = 0
        while index < len(s) and s[index] == 'x':
            index += 1
        while index < len(s):
            if s[index] == 'x':
                if s[index - 1] == 'x' and s[index - 2] == 'x':
                    return index
            index += 1
        return None

    def remove_char_at_index(s, index):
        return s[:index] + s[index+1:]

    def remove_first_xxx(s):
        i = find_next_xxx_index(s)
        if i is None:
            return s
        return remove_char_at_index(s, i)

    result = len(s)
    while True:
        s = remove_first_xxx(s)
        result = min(result, len(s))
        i = find_next_xxx_index(s)
        if i is None:
            return result
        s = remove_char_at_index(s, i)
        result = min(result, len(s))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
