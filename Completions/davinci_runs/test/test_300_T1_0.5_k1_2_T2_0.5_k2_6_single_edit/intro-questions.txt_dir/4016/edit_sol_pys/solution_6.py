
def main():
    n = int(input())
    t = input()
    print(t[0] + t[1:].replace("L", " ").replace("R", "L").replace(" ", "R"))


if __name__ == "__main__":
    main()
