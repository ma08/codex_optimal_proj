

def main():
    n, r = map(int, input().split())  # n: number of projects, r: initial rating
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # 0: rating, 1: bonus
    projects.sort(key=lambda x: x[1])  # sort by bonus
    count = 0
    for project in projects:
        if r >= project[0]:
            r += project[1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()
