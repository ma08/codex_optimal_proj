

def main():
    a, b, c, d = map(int, input().split()) #a, b, c, dを入力する．
    print(max(a * c, a * d, b * c, b * d)) #a*c, a*d, b*c, b*dのうち最大のものを出力する．

if __name__ == '__main__':
    main()
