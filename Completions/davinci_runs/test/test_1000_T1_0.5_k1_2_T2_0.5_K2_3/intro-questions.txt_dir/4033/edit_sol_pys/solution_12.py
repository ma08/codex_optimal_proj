

def main():
    a, b = map(int, input().split())  # mapでint型に変換

    if a == b:
        print(4 * b)
    else:
        print(2 * (b + a))

if __name__ == "__main__":
    main()
