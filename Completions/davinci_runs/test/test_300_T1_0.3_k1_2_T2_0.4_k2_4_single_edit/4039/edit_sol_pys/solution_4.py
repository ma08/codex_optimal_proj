

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))
    projects.sort(key=lambda x: x[0])
    for i in range(n):
        if r < projects[i][0]:
            print("No")
            break
        else:
            r += projects[i][1]
            if r < 0:
                print("No")
                break
            if i == n - 1:
                print("Yes")

main()
