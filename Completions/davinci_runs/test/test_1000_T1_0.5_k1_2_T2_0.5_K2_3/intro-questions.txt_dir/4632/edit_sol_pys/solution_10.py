

def main():
    num_cases = int(input())
    for i in range(num_cases):
        num_packages = int(input())
        packages = []
        for j in range(num_packages):
            coords = input().split(' ')
            packages.append((int(coords[0]), int(coords[1])))

        packages.sort(key=lambda x: (x[0], x[1]))

        last_x = 0
        last_y = 0
        path = ""
        try:
            for p in packages:
                if p[0] < last_x or p[1] < last_y:
                    raise ValueError

                path += "R" * (p[0] - last_x)
                path += "U" * (p[1] - last_y)
                last_x = p[0]
                last_y = p[1]

            print("YES")
            print(path)

if __name__ == "__main__":
    main()
