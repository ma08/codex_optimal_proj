
#

def string_to_list():
    global n, string_list
    n = int(input())
    string_list = list(input())


def xxx_check():
    global xxx_counter
    xxx_counter = 0
    for i in range(len(string_list)-2):
        if string_list[i] == "x" and string_list[i+1] == "x" and string_list[i+2] == "x":
            xxx_counter += 1


def xxx_check_output():
    if xxx_counter == 0:
        print(0)
    else:
        print(xxx_counter)


def main():
    string_to_list()
    xxx_check()
    xxx_check_output()


if __name__ == "__main__":
    main()
