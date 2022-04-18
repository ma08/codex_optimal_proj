

def main():
    s = raw_input()
    str_list = []
    for char in s:
        if char == '<':
            str_list.pop()
        else:
            str_list.append(char)
    print("".join(str_list))

if __name__ == '__main__':
    main()
