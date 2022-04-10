

n = int(input())
s = input()

def valid_brackets(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack

def count_swaps(s):
    count = 0
    for i in range(n):
        if s[i] == "(":
            count += 1
    return min(count, n - count)

if valid_brackets(s):
    print(count_swaps(s))
else:
    print(0)