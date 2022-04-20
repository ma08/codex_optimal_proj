
def get_number_of_brackets_to_change(s):
    opening_brackets = []
    number_of_brackets = 0

    for i, bracket in enumerate(s):
        if bracket == "(":
            opening_brackets.append(bracket)
        elif bracket == ")":
            if len(opening_brackets) == 0:
                number_of_brackets += 1
            else:
                opening_brackets.pop()
        else:
            pass
    number_of_brackets += len(opening_brackets)
    return number_of_brackets

if __name__ == "__main__":
    s = input()
    print(get_number_of_brackets_to_change(s))
