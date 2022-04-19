
def main():
    n, r = map(int, input().split())  # n is number of projects, r is initial rating
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # first element is rating change, second is time
    projects.sort(key=lambda x: x[1])
    for project in projects:
        if r >= project[0]:
            r += project[1]
            if r < 0:
                print("NO")
                return
    print("YES")

if __name__ == '__main__':
    main()
