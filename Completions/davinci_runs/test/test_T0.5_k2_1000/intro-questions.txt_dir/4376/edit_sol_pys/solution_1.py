
# coding: utf-8

def get_room_info(n, m, a_list, b_list):
    a_sum = a_list[0]
    f = 1
    k = 0
    for i in range(n):
        if b_list[0] <= a_sum:
            print(f, b_list[0] - k)
        else:
            a_sum += a_list[i + 1]
            i += 1
            f = i + 1
            k = b_list[0] - a_list[i]
            print(f, b_list[0] - k)
    for j in range(1, m):
        if b_list[j] <= a_sum:
            print(f, b_list[j] - k)
        else:
            a_sum += a_list[i + 1]
            i += 1
            f = i + 1
            k = b_list[j] - a_list[i]
            print(f, b_list[j] - k)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    get_room_info(n, m, a_list, b_list)
