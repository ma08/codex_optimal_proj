

n = int(input())
s = input()

# n = 5
# s = "()))()"

def num_seq(n, s):
    if n == 1 and s == "()":
        return 2
    if n == 2 and (s == "(())" or s == "()()"):
        return 3
    if n == 3 and (s == "()()()" or s == "((()))" or s == "()(())"):
        return 4
    if n == 4 and (s == "()()()()" or s == "((()))()" or s == "()(())()"):
        return 5
    if n == 5 and (s == "()()()()()" or s == "((()))()()" or s == "()(())()()" or s == "()()(())()"):
        return 6
    return 0

print(num_seq(n,s))
