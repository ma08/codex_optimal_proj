

def main():
    a, b, c = input().split()  # a, b, c = кот, ток, торт  # a[-1] == b[0] - проверка последнего символа в a на совпадение с первым символом в b
    if a[-1] == b[0] and b[-1] == c[0]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
