

def main():
    num_cases = int(input())
    for i in range(num_cases):
        num_packages = int(input())
        packages = []
        for _ in range(num_packages):
            coords = input().split(' ')
            packages.append((int(coords[0]), int(coords[1])))

        packages.sort(key=lambda x: (x[0], x[1]))
        if packages[0][1] > 0:
            print("NO")
            continue

        last_x = 0
        last_y = 0
        path = ""
        for package in packages:
            if package[0] < last_x or package[1] < last_y:
                print("NO")
                break

                break

            path += "R" * (package[0] - last_x)
            path += "U" * (package[1] - last_y)
            last_x = package[0]
            last_y = package[1]
        else:
            print("YES")
            print(path)

if __name__ == "__main__":
    main()
