
def get_closing_bracket_positions(s):
    closing_brackets = []
    for i, bracket in enumerate(s):
        if bracket == ")":
            closing_brackets.append(i)
    return closing_brackets

def get_opening_bracket_positions(s):
    opening_brackets = []
    for i, bracket in enumerate(s):
        if bracket == "(":
            opening_brackets.append(i)
    return opening_brackets


def get_number_of_brackets_to_change(s):
    opening_brackets = get_opening_bracket_positions(s) # [1, 3, 5, 7]
    closing_brackets = get_closing_bracket_positions(s) # [2, 4, 6, 8]

    number_of_brackets = 0

    while len(opening_brackets) > 0 and len(closing_brackets) > 0:
        if opening_brackets[0] < closing_brackets[0]: # 1 < 2
            opening_brackets.pop(0)
        else: # 2 > 1

            number_of_brackets += 1
            closing_brackets.pop(0)
    return number_of_brackets

if __name__ == "__main__":
    s = input()
    print(get_number_of_brackets_to_change(s))
