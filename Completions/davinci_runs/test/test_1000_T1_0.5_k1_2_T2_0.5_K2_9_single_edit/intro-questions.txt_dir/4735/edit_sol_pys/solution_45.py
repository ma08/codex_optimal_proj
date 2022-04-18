

def main():
    name = input()
    name_list = name.split()
    for i in range(len(name_list)):
        name_list[i] = name_list[i].capitalize()
        name = " ".join(name_list)

    print(name)

if __name__ == "__main__":
    main()
