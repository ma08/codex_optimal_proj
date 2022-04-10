

def main():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(tuple(map(int, input().split())))

    # sort by a_i (ascending order)
    projects.sort(key=lambda x: x[0])

    # start with the lowest a_i
    for a_i, b_i in projects:
        if r < a_i:
            print("NO")
            return
        r += b_i
        if r < 0:
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    main()