

def main():
    K = int(input())
    i = 1
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        while True:
            if (7 * (10 ** i) - 7) % K == 0:
                print(i + 1)
                break
            i += 1

if __name__ == '__main__':
    main()
