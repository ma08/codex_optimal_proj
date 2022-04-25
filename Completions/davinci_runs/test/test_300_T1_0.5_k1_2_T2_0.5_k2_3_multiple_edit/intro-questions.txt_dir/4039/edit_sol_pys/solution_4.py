

import sys

def main():
    n, r = map(int, input().split()) # n is number of projects and r is the initial amount
    projects = []
    for i in range(n):
        projects.append(list(map(int, input().split())))

    projects.sort(key=lambda x: x[1])

    for i in range(n):
        if projects[i][0] > r: # if the amount needed is greater than the initial amount, then no
            print("NO")
            sys.exit()
        r += projects[i][1]
        if r < 0:
            print("NO")
            sys.exit()
    print("YES")

if __name__ == '__main__':
    main()
