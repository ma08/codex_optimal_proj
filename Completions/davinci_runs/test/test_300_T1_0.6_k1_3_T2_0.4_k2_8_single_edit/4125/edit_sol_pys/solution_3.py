
def main():
    n, x = map(int, input().split())
    x_list = sorted(list(map(int, input().split())) + [x])
    d_list = []
    for i in range(n):
        d_list.append(x_list[i + 1] - x_list[i])  # 差分を取る
    print(max(d_list) // 2)

if __name__ == '__main__':
    main()
