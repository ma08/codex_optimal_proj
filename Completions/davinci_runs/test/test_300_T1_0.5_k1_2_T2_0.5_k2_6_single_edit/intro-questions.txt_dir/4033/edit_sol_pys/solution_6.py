

def main():
    a, b = map(int, input().split()) # aとbに入力された値を代入

    if a == b: # aとbが等しいとき
        print(4 * a)
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
