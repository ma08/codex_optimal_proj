
# This is a comment

def main():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))
    ans = 0
    while len(problems):
        if problems[0] <= k and problems[-1] <= k:
            if problems[0] <= problems[-1]:
                problems.pop(0)
            else:
                problems.pop()
            ans += 1
            problems.pop(0)
        elif problems[-1] <= k:
            ans += 1
            problems.pop()
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
