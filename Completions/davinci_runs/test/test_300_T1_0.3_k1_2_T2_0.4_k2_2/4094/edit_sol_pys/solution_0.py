

def main():
    K = int(input())
    i = 1
    while True:
        if (7 * (10 ** i) - 7) % K == 0:  # 7777...7(i桁) % K = 0
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
