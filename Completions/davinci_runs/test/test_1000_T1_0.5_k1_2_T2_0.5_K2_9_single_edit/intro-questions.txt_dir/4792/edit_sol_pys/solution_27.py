

def remove_duplicates(input_string):
    new_name = ""

    for i in range(len(input_string)):
        if i == 0:
            new_name += input_string[0]
        elif input_string[i] != input_string[i-1]:
            new_name += input_string[i]

    return new_name


if __name__ == "__main__":
    name = input()
    print(remove_duplicates(name))
