

def main():
    a, b, c = [int(x) for x in input().split()]  # a,b,cを受け取る
    print("Yes" if a + b > c else "No")  # a+b>cならYes、それ以外はNo

if __name__ == '__main__':
    main()
