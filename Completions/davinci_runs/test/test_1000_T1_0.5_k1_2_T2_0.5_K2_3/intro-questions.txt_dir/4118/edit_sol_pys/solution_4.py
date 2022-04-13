

def main():
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if num1 > 20 or num1 < 1 or num2 > 20 or num2 < 1 or num1 + num2 > 21:
        print(-1)
        return
    print(num1 * num2)

if __name__ == '__main__':
    main()
