

def main():
    n, r = map(int, input().split())  # n is the number of projects and r is the initial rating
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # list of projects
    projects.sort(key=lambda x: x[1])
    count = 0
    for project in projects:
        if r >= project[0]:  # if the rating is greater than the minimum rating required for the project
            r += project[1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()
