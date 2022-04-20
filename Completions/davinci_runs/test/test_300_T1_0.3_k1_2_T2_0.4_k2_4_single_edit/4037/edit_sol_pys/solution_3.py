
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, sys.stdin.readline().split())))
    projects = sorted(projects, key=lambda x: x[0])
    count = 0
    for project in projects:
        if project[0] > r:
            break
        r += project[1]
        if r < 0:
            break
        count += 1
    print(count)

if __name__ == '__main__':
    main()
