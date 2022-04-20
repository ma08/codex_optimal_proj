

def main():
    """Mishka and the Contest"""
    num_problems, solving_skill = map(int, input().split())
    problems = list(map(int, input().split()))
    problems_solved = 0
    while problems:
        if problems[0] <= solving_skill:
            problems.pop(0)
            problems_solved += 1
        elif problems[-1] <= solving_skill:
            problems.pop()
            problems_solved += 1
        else:
            break
    print(problems_solved)

if __name__ == '__main__':
    main()