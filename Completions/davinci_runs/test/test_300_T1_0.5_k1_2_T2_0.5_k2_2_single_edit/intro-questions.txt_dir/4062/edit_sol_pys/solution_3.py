
def main():
    a, b, c, d = map(int, input().split())  # 分割数字
    print(max(a * c, a * d, b * c, b * d))

if __name__ == '__main__':
    main()
