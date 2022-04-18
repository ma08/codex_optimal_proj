import sys



def main():
    n = int(input())
    for i in range(n):
        k = int(input())
        name = input()
        for j in range(k):
            item = input()
            if item == "pea soup":
                for l in range(k):
                    item = input()
                    if item == "pancakes":
                        print(name)
                        sys.exit()


if __name__ == "__main__":
    main()
