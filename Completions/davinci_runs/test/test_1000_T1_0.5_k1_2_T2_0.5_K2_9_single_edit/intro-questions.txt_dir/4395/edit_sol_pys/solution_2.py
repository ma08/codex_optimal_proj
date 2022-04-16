

# SOLUTION
# We know that there are three colors, so we can just try all three colors and see which one gives us the best answer.
# We can do this by iterating through the string and checking if the current color is the same as the next color.
# If it is, we need to change it to one of the other colors.
# The only question is which color should we change it to.
# We can use the color that is the furthest away.
# For example, if we have "RRRR", we should change it to "GRGR", since the color furthest away is green.
# We can do this by keeping track of the index of the last occurrence of each color.
# If we have "RRRR", we should change it to "GRGR", since the color furthest away is green. We can do this by keeping track of the index of the last occurrence of each color.

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = input()
    last = {'R': -1, 'G': -1, 'B': -1}
    ans = [None] * n
    res = n
    for i in range(n):
        c = s[i]
        a = 'R' if c != 'R' else 'G' if last['G'] < last['B'] else 'B'
        if last[a] < i - 1:
            last[a] = i
            ans[i] = a
        else:
            a = 'G' if c != 'G' else 'R' if last['R'] < last['B'] else 'B'
            if last[a] < i - 1:
                last[a] = i
                ans[i] = a
            else:
                a = 'B' if c != 'B' else 'R' if last['R'] < last['G'] else 'G'
                if last[a] < i - 1:
                    last[a] = i
                    ans[i] = a
                else:
                    res = min(res, i + 1)
                    break
    if res == n:
        print(0)
        print(s)
    else:
        print(res)
        print(''.join(ans[:res]))

main()
