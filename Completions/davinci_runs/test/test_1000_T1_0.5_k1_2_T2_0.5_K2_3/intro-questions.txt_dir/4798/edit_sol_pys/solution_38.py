

def main():
    name = input()
    print(name[0] + "".join([x[0] for x in name.split("_")]))

if __name__ == "__main__":
    main()
