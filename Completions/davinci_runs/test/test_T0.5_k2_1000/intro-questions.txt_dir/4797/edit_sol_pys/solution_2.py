
def main():
    string = input()
    string_list = []
    for i in string:
        if i == '<':
            string_list.pop()
        else:
            string_list.append(i)
    print("".join(string_list))

if __name__ == '__main__':
    main()
