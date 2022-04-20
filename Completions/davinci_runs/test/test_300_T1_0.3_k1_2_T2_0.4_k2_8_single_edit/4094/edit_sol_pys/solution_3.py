

def main():
    K = int(input())
    i = 1
    while True:
        if (7 * (10 ** i) - 7) % K == 0:  # 7のi乗の余りが0になる最小のi
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
