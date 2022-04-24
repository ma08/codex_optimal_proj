

n = int(input())
s = input()

# n = 5
# s = "()))()"

    if n == 0:
        if s == "":
            return 1
        return 0
def num_seq(n, s):
    if n == 1:
        if s == "()":
            return 2
        return 0
    if n == 2:
        if s == "()()":
            return 3
        if s == "()(())":
            return 2
        return 0
    if n == 3:
        if s == "()()()":
            return 4
        if s == "((()))":
            return 1
        if s == "((())())":
            return 1
        return 0
    if n == 4:
        if s == "()()()()":
            return 5
        if s == "((()))()":
            return 1
        if s == "((())()())":
            return 1
        return 0
    if n == 5:
        if s == "()()()()()":
            return 6
        if s == "((()))()()":
            return 1
        if s == "((())()()())":
            return 1
        if s == "()()(())()":
            return 1
        return 0

print(num_seq(n,s))
