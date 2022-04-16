

def main():
    s = input()
    s_list = s.split('<')
    for i in range(len(s_list)):
        s_list[i] = s_list[i].split('>')
    s_list = [i for j in s_list for i in j]
    print(s_list)
    result = []
    for i in s_list:
        if i == '':
            result.pop()
        elif i == ' ':
            pass
        else:
            result.append(i)
    print(''.join(result))

if __name__ == '__main__':
    main()
