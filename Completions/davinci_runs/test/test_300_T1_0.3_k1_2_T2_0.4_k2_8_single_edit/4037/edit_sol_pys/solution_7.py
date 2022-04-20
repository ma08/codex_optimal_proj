

def main():
    n, r = map(int, input().split())  # n is number of projects, r is initial rating
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # append a list of [difficulty, rating]
    projects.sort(key=lambda x: x[1])  # sort by rating
    count = 0
    for project in projects:
        if r >= project[0]:
            r += project[1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()
