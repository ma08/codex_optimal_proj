# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    # 2つの整数 a, b が与えられます。
    # a ÷ b のあまりを求めてください。
    a, b = map(int, input().split())
    print(a % b)


if __name__ == '__main__':
    main()



def main():
    # スペース区切りの整数 n, l が与えられます。
    # n 個の苺が並んでいて、苺 i の長さは l + i - 1 です。
    # これらの苺を 1 本ずつ食べていき、苺の長さの総和を求めてください。
    # ただし、苺 i を食べるときは、それより左にある苺はすべて食べる必要があります。
    n, l = map(int, input().split())
    flavor_list = [l + i for i in range(n)]
    print(sum(flavor_list[1:]))


if __name__ == "__main__":
    main()
