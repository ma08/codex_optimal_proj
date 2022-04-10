

def main():
    k = int(input())
    count = 0
    i = 0
    while count < k:
        i += 1
        count = 7 * (10**i)
        if count % k == 0:
            print(i+1)
            return
    print(-1)

if __name__ == '__main__':
    main()