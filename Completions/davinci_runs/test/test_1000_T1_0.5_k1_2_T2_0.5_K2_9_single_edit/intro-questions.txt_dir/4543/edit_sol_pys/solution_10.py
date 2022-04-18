

def is_square(n):
    return int(n**0.5)**2 == n


def main():
    a, b = map(int, input().split())

    if is_square(int(str(a) + str(b))):  # 判定
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
