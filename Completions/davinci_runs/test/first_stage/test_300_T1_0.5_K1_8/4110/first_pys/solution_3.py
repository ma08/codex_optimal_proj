

import sys

def main():
    D, G = map(int, sys.stdin.readline().split())
    problems = []
    for i in range(D):
        problems.append(list(map(int, sys.stdin.readline().split())))
    problems.reverse()
    ans = 0
    now = 0
    while True:
        if now >= G:
            break
        if problems[0][0] != 0:
            problems[0][0] -= 1
            now += problems[0][1] + 100 * (D - len(problems) + 1)
            ans += 1
        else:
            problems.pop(0)
    for i in range(len(problems)):
        if problems[i][0] == 0:
            continue
        if now < G:
            if (G - now) % (100 * (D - i)) == 0:
                ans += (G - now) // (100 * (D - i))
                now = G
            elif (G - now) <= ((100 * (D - i)) * problems[i][0]):
                ans += (G - now) // (100 * (D - i)) + 1
                now = G
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()