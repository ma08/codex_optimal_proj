

def main():
    n, x = map(int, input().split())
    x_list = sorted(list(map(int, input().split())) + [x])
    d_list = []
    for i in range(len(x_list) - 1):
        d_list.append(x_list[i + 1] - x_list[i])
    print(max(d_list) // 2)

if __name__ == '__main__':
    main()
