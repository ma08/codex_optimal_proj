

def main():
    L, H = map(int, input().split()) # L, HはそれぞれLとHを示す
    count = 0
    for i in range(L, H + 1): # iはLからHまでの値を示す
        if len(set(str(i))) == 6: # 6桁の数字である
            if i % 2 != 0 and i % 5 != 0: # 2でも5でも割り切れない数字である
                if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0: # 各桁の数字で割り切れる数字である
                count += 1
    print(count)

main()
