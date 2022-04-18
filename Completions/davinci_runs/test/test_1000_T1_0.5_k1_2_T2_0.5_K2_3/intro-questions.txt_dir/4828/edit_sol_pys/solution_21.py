

def main():
    """
    Main function
    """
    code = input()  # input string
    nop_count = 0  # number of nop's
    for index in range(len(code)):
        if code[index].isupper():
            if index % 4 != 0:  # if current index is not divisible by 4
                nop_count += 4 - (index % 4)
    print(nop_count)  # print result

if __name__ == "__main__":
    main()
