import sys
from typing import List

def main():
    n, r = map(int, input().split())
    projects: List[List[int]] = []
    for i in range(n):
        projects.append(list(map(int, input().split())))

    projects.sort(key=lambda x: x[1])

    for i in range(n):
        if projects[i][0] > r:
            print("NO")
            exit()
        r += projects[i][1]
        if r < 0:
            print("NO")
            exit()

    print("YES")

if __name__ == '__main__':
    main()
