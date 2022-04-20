

def main():
    K = int(input())
    i = 1
    while True:
        if (7 * (10 ** i) - 7) % K == 0:  # 7のi乗-7をKで割った余りが0ならば
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
