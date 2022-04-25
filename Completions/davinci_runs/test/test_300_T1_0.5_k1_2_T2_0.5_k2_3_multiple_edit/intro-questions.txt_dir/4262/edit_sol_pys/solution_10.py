# 入力
N = int(input())
P = list(map(int, input().split()))  # P[i]はi番目の花の色
Q = list(map(int, input().split()))  # Q[i]はi番目の花の色


def bubble_sort(arr):
    count = 0
    for i in range(N):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return count


def main():
    count_P = bubble_sort(P)
    count_Q = bubble_sort(Q)
    print(count_P + count_Q)


if __name__ == '__main__':
    main()
