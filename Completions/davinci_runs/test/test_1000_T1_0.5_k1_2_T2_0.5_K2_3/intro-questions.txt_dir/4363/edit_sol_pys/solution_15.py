

def main():
    k, s = map(int, input().split()) #mapでリストを作成
    count = 0
    for x in range(k+1): #range(k+1)で0からkまでの数値を取得
        for y in range(k+1): #range(k+1)で0からkまでの数値を取得
            for z in range(k+1): #range(k+1)で0からkまでの数値を取得
                if x + y + z == s:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()
