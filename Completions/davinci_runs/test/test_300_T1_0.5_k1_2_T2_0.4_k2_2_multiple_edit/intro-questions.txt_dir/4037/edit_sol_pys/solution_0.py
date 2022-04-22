

def main():
    n, r = map(int, input().split()) # n is the number of projects and r is the amount of money
    projects = []
    for i in range(n):
        a, b = map(int, input().split()) # a is the cost and b is the benefit
        projects.append((a, b))

    projects.sort(key = lambda x: x[0])

    count = 0
    for project in projects:
        if r >= project[0]: # if the money is enough to buy the project
            r += project[1]
            count += 1
        else:
            break

    print(count)

if __name__ == '__main__':
    main()
