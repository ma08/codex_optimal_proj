# coding: utf-8

    """
    横幅を受け取って，横幅に応じて大きさを変えた三角形を出力する
    """
def main():
    n = int(input())
    a = list(map(int, input().split()))
    sort_a = sorted(a)

    for i in range(n):
        print(" " * (sort_a[i] - 1) + "#" * sort_a[i])

main()
