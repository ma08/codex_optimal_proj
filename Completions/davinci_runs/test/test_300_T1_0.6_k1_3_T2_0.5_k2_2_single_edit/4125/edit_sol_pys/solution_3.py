

def main():
    n, x = map(int, input().split())
    x_list = [x] + list(map(int, input().split()))
    x_list.sort()  # xを含むリストをソート
    d_list = []
    for i in range(len(x_list) - 1):  # 各要素とその次の要素の差をリストに格納
        d_list.append(x_list[i + 1] - x_list[i])
    print(max(d_list) // 2)

if __name__ == '__main__':
    main()
