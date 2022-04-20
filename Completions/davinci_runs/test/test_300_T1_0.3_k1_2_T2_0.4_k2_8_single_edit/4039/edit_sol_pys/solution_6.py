

def main():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[1])
    for i in range(len(projects)):
        if r >= projects[i][0]:
            r += projects[i][1]
            if r < 0: return print("NO")
    print("YES")

if __name__ == '__main__':
    main()
