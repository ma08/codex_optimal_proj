

def main():
    a, b, c, d = map(int, input().split()) # a = 縦, b = 横, c = 縦, d = 横 
    print(max(a * c, a * d, b * c, b * d)) # 縦 * 縦, 縦 * 横, 横 * 縦, 横 * 横

if __name__ == '__main__':
    main()
