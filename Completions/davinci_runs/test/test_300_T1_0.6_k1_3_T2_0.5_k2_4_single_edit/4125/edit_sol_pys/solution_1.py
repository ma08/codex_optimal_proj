
def main():
    n, x = map(int, input().split())
    x_list = [x] + list(map(int, input().split()))
    x_list.sort()  # [1, 2, 3, 4, 5]
    d_list = [x_list[i + 1] - x_list[i] for i in range(len(x_list) - 1)]
    print(max(d_list) // 2)  # 3

if __name__ == '__main__':
    main()
