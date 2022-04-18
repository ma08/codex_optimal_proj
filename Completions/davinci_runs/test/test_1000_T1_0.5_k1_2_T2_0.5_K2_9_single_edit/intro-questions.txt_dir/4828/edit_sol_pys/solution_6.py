

def main():
    """
    Main function
    """
    code = input("")
    nop_count = 0
    for index in range(len(code)):
        if code[index].isupper():
            if index % 4 != 0:
                nop_count += 4 - (index % 4)
    print(nop_count)


if __name__ == "__main__":
    main()
