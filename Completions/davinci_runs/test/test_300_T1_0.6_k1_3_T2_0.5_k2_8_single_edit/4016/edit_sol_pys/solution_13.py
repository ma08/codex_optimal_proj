

def main():
    n, k = [int(x) for x in input().split()] #n,kをそれぞれint型に変換して受け取る
    t = input() #文字列tを受け取る
    s = t
    while len(s) < k * n:
        s += t #k*n文字になるまでtを足す
    print(s[:k * n])

if __name__ == '__main__': #これがないとmain()が実行されない
    main()
