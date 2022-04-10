

def test_easy():
    assert solve_easy("abacbecfd") == "001010101"
    assert solve_easy("aaabbcbb") == "01011011"
    assert solve_easy("abcde") == "00000"


def solve_easy(s):
    # First, check if the string is already sorted
    if sorted(s) == list(s):
        return "0" * len(s)
    # Second, check if the string is unsortable
    if sorted(s) != list(s):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return "NO"
    # Otherwise, return the sortable string
    s_list = list(s)
    for i in range(len(s_list) - 1):
        if s_list[i] > s_list[i + 1]:
            s_list[i + 1] = s_list[i]
    return "".join(str(x) for x in s_list)


if __name__ == "__main__":
    s = input()
    print(solve_easy(s))