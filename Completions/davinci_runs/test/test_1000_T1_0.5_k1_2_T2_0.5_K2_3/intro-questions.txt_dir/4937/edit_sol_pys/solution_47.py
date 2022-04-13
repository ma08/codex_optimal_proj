import sys

def main():
    n, a = map(int, sys.stdin.readline().split()) #n:枚数 a:枚数の合計
    e = list(map(int, sys.stdin.readline().split())) #e:各枚の価値
    e.sort() #昇順にソート
    e.reverse() #降順にソート
    count = 0
    for i in e:
        if a >= i:
            count += 1
            a -= i
    print(count)

if __name__ == '__main__':
    main()
