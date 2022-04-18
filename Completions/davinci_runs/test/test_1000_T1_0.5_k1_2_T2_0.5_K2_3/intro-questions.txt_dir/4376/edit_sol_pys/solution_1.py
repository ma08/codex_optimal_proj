


def get_room_info(n, m, a_list, k_list):
    a_sum = 0
    for i in range(n):
        a_sum += a_list[i]
        if k_list[0] <= a_sum:
            break
    f = i
    k = k_list[0] - a_list[i]
    for j in range(1, m):
        if k_list[j] <= a_sum:
            print(f+1, k_list[j] - k)
        else:
            a_sum += a_list[i+1]  # 前のループでiはインクリメントされている
            i += 1
            f = i
            k = k_list[j] - a_list[i]
            print(f+1, k)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    k_list = list(map(int, input().split()))
    get_room_info(n, m, a_list, k_list)
