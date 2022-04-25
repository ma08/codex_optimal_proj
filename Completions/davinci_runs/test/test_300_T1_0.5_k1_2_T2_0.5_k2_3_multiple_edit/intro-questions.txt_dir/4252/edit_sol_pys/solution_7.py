

def get_result(n, s):
    def find_next_xxx_index(s_, start_index=0):
        index = start_index
        while index < len(s_) and s_[index] == 'x':
            index += 1
        while index < len(s_):
            if s_[index] == 'x':
                if s_[index - 1] == 'x' and s_[index - 2] == 'x':
                    return index
            index += 1
        return -1

    def remove_char_at_index(s_, index):
        return s_[:index] + s_[index+1:]

    def remove_first_xxx(s_):
        i = find_next_xxx_index(s_)
        if i == -1:
            return s_
        return remove_char_at_index(s_, i)

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
