
def main():
    input_num = int(input())
    for _ in range(input_num):
        menu_num = int(input())
        menu_list = []
        for _ in range(menu_num):
            menu_list.append(input())
        if 'pea soup' in menu_list and 'pancakes' in menu_list:
            print(menu_list[menu_list.index('pea soup')])
            break
    else:
        print('Anywhere is fine I guess')

if __name__ == "__main__":
    main()
