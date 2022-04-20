


def string_to_list(n):
    string_list = list(input("Enter your string: "))
    return string_list


def xxx_check(string_list):
    xxx_counter = 0
    for i in range(len(string_list)-2):
        if string_list[i] == "x" and string_list[i+1] == "x" and string_list[i+2] == "x":
            xxx_counter += 1


def xxx_check_output(xxx_counter):
    if xxx_counter == 0:
        print(0)
    else:
        print(xxx_counter)


def main():
    n = int(input("Enter the length of your string: "))
    string_list = string_to_list(n)
    xxx_counter = xxx_check(string_list)
    xxx_check_output(xxx_counter)


if __name__ == "__main__":
    main()
