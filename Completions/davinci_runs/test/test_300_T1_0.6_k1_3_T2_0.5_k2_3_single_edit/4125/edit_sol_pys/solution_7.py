

def main():
    n, x = map(int, input().split())  # n: 入力回数、x: 中央値
    x_list = list(map(int, input().split()))  # x_list: 入力される数字のリスト
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(len(x_list) - 1):
        d_list.append(x_list[i + 1] - x_list[i])
    print(max(d_list) // 2)

if __name__ == '__main__':
    main()
