

def main():
    input_num = int(input())
    for _ in range(input_num):
        menu_num = int(input())
        menu_list = []
        for _ in range(menu_num):
            menu_list.append(input())
        menu_list = [menu.lower() for menu in menu_list]
        if 'pea soup' in menu_list and 'pancakes' in menu_list:  # 両方ともある場合
            print(menu_list[menu_list.index('pea soup')])  # 先に見つかった方を出力
            break
    else:
        print('Anywhere is fine I guess')

if __name__ == "__main__":
    main()
