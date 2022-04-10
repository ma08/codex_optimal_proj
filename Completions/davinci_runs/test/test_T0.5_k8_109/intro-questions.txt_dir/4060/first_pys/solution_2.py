

def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def solve(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
        if is_valid(s):
            ans += 1
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return ans

def main():
    n = int(input())
    s = input()
    print(solve(list(s)))

if __name__ == '__main__':
    main()