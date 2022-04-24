import math

def main():
    n = int(input())
    r = math.ceil(math.sqrt(n))
    for i in range(r, 0, -1):  # iはnの約数
        if n % i == 0:
            print(n // i // 10 ** (len(str(i)) - 1))  # 最上位の桁を出力
            break

if __name__ == '__main__':
    main()
