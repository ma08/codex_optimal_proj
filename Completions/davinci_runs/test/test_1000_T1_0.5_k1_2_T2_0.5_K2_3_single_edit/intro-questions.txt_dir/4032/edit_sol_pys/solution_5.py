
def main():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))
    cnt = 0
    while len(problems) > 0:
        if problems[0] <= k:
            cnt += 1
            problems.pop(0)
        elif problems[-1] <= k:
            cnt += 1
            problems.pop()
        else:
            break
    print(cnt)





if __name__ == '__main__':
    main()
