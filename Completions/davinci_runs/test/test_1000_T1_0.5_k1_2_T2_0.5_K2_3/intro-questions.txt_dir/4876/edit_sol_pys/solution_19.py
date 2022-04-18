

def main():
    input_num = int(raw_input())
    for i in range(input_num):
        menu_num = int(raw_input())
        menu_list = []
        for _ in range(menu_num):
            menu_list.append(raw_input())
        if 'pea soup' in menu_list and 'pancakes' in menu_list:  # check if both items are on the menu
            print(menu_list[0])
            break  # break out of the loop if we found the correct menu
    else:
        print('Anywhere is fine I guess')

if __name__ == "__main__":
    main()
