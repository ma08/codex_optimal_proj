
def main():
    s = input()
    s_temp = ''
    for i in s:
        if i == '<':
            s_temp = s_temp[:-1]
        else:
            s_temp += i
    print(s_temp)

if __name__ == '__main__':
    main()
