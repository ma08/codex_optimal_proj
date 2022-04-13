

def main():
    num_packages = int(input())  # number of test cases
    for i in range(num_packages):
        num_packages = int(input())  # number of packages
        packages = []
        for j in range(num_packages):
            coords = input().split(' ')  # coordinate of package
            packages.append((int(coords[0]), int(coords[1])))

        packages.sort(key=lambda x: (x[0], x[1]))
        if packages[0][1] > 0:
            print("NO")
            continue

        last_x = 0
        last_y = 0
        path = ""
        for p in packages:
            if p[0] < last_x or p[1] < last_y:
                print("NO")
                break

            path += "R" * (p[0] - last_x)
            path += "U" * (p[1] - last_y)
            last_x = p[0]
            last_y = p[1]
        else:
            print("YES")
            print(path)

if __name__ == "__main__":
    main()
