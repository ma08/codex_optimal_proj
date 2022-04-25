

def main():
    a, b, c, d = map(int, input().split()) # a:高さ b:横幅 c:高さ d:横幅 (a, b)と(c, d)のどちらが大きいか比較
    print(max(a * c, a * d, b * c, b * d))

if __name__ == '__main__':
    main()
