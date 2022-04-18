

def main():
    s = input().strip()
    s_list = []
    for i in s:
        if i == '<':
            s_list.pop()
        else:
            s_list.append(i)
    print("".join(s_list))

if __name__ == '__main__':
    main()
