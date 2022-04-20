

def main():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[1], reverse=True)
    count = 0
    for project in projects:
        if r > project[0]:
            r += project[1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()
