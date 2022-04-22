

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))

    projects.sort(key=lambda x: x[1])

    if any([project[0] > r for project in projects]):
        return "NO"
    else:
        for i in range(n):
            r += projects[i][1]
            if r < 0:
                return "NO"
    return "YES"

if __name__ == '__main__':
    print(main())
