
def main():
    name = input()
    print(name[0] + "".join([x[0] for x in name.split("-")[1:]]))


if __name__ == "__main__":
    main()
