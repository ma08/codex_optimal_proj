

def main():
    a, b = map(int, input().split())  # splitで改行区切りで入力してる

    if a == b:
        print(4 * a)
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
