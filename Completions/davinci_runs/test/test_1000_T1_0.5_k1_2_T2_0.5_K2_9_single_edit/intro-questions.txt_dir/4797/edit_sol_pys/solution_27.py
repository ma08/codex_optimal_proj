

def main():
    s_input = input()
    s_list = list(s_input)
    for i in s_list:
        if i == '<':
            s_list.pop()
        else:
            s_list.append(i)
    print("".join(s_list), end='')

if __name__ == '__main__':
    main()
