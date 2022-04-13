
def main():
    # needs a file name
    name = input()
    # prints the first letter of each word in the file name
    print(name[0] + "".join([x[0] for x in name.split("-")[1:]]))

if __name__ == "__main__":
    main()
