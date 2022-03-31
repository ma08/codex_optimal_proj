

def solve():
    n = int(input())
    s = input()
    left = 0
    right = 0
    for i in range(n):
        if s[i] == '(':
            left += 1
        else:
            if left > 0:
                left -= 1
            else:
                right += 1
    print(2 * (left + right))

solve()
