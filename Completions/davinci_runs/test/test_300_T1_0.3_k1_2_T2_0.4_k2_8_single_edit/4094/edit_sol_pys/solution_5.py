

def main():
    K = int(input())
    i = 1
    while True:
        if (7 * (10 ** i) - 7) % K == 0:  # Kの倍数になる最小の数を求める
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
