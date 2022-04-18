
def main():
    file = open("text.txt", "r")


    for line in file:
        print(line)

    file.close()


if __name__ == "__main__":
    main()
