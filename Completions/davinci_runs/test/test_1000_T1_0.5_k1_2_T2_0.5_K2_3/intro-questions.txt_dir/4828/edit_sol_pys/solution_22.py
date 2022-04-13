

def main():
    """
    Main function
    """
    code = input()  # input code
    nop_count = 0  # no of padding characters
    for index in range(len(code)):
        if code[index].isupper():
            if index % 4 != 0:
                nop_count += 4 - (index % 4)
    print(nop_count)

if __name__ == "__main__":
    main()
