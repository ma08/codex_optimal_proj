

def main():
    a, b = map(int, input().split())  # a*bの大きさの正方形を作る
    if a == 1 or b == 1:  # aとbのどちらかが1ならばそれをかければよい
        print(a * b)
    elif a == 2:  # aが2ならばbが2,3,5,7,11ならばa*bが作れる
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11:
            print(a * b)
        else:
            print(-1)
    elif a == 3:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11:  # aが3ならばbが2,3,5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 4:
        if b == 3 or b == 5 or b == 7 or b == 11:  # aが4ならばbが3,5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 5:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11:  # aが5ならばbが2,3,5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 6:
        if b == 5 or b == 7 or b == 11:  # aが6ならばbが5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7 or b == 11:  # aが7ならばbが2,3,5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 8:
        if b == 3 or b == 5 or b == 7 or b == 11:  # aが8ならばbが3,5,7,11ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    elif a == 9:
        if b == 2 or b == 3 or b == 5 or b == 7:  # aが9ならばbが2,3,5,7ならばa*bが作れる
            print(a * b)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
