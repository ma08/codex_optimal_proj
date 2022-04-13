
def solve(n, k, string):
    string = list(string)
    while k > 0:
        changed = False
        for i in range(n-1):
            if string[i] > string[i+1]:
                string[i], string[i+1] = string[i+1], string[i]
                k -= 1
                changed = True
                break
        if not changed:
            break
    return "".join(string)

for _ in range(int(input())):
    n, k = map(int, input().split())
    string = input()
    print(solve(n, k, string))
