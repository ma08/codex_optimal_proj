

def main():
    name = input().split("-")
    print(name[0][0] + "".join([x[0] for x in name[1:]]))


if __name__ == "__main__":
    main()
