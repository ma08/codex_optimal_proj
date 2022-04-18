

def main():
    x = input()
    y = input()
    if x > 20 or x < 1 or y > 20 or y < 1 or x.isdigit() == False or y.isdigit() == False:
        print(-1)
        return
    x = int(x)
    y = int(y)
    print(x + y)

if __name__ == '__main__':
    main()
