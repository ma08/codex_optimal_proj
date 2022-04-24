

def main():
    n, x = map(int, input().split())
    x_list = [x] + list(map(int, input().split()))
    x_list.sort(reverse=True)
    d_list = []
    for i in range(len(x_list) - 2):
        d_list.append(x_list[i + 1] - x_list[i + 2])
    print(max(d_list) // 2)

if __name__ == '__main__':
    main()
