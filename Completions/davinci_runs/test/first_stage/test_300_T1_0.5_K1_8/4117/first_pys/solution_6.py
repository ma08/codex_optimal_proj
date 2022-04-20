

import sys

def main():
    """
    1. 入力を受け取る
    2. 三角形を作れるかどうかを判定する
    3. 三角形を作れるかどうかを判定する関数を作成する
    4. 組み合わせを数える
    """
    num_of_sticks = int(input())
    sticks = list(map(int, input().split()))
    # print(num_of_sticks)
    # print(sticks)

    # for i in range(num_of_sticks):
    #     print(sticks[i])

    count = 0
    for i in range(num_of_sticks - 2):
        for j in range(i + 1, num_of_sticks - 1):
            for k in range(j + 1, num_of_sticks):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[k] != sticks[i]:
                    if is_triangle(sticks[i], sticks[j], sticks[k]):
                        count += 1
    print(count)

def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

if __name__ == "__main__":
    main()