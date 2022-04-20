

def main():
    s = input()
    s_list = list(s)
    count = 0
    for i in range(len(s_list)-1):
        if s_list[i] == s_list[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()