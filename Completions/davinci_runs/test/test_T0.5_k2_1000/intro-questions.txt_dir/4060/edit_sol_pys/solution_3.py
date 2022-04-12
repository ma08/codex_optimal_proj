

n = int(input())
s = input()

# check if the sequence is already regular
def is_regular(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

# count the number of opening and closing brackets
def count_brackets(s):
    opening = 0
    closing = 0
    for char in s:
        if char == '(':
            opening += 1
        else:
            closing += 1
    return opening, closing

def count_changes(s):
    if is_regular(s):
        return 0
    opening, closing = count_brackets(s)
    if opening == closing:
        return 0
    return opening + closing - abs(opening - closing)

print(count_changes(s))
