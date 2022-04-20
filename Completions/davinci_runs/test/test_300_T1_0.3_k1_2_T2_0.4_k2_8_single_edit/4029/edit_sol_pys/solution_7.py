

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        n = str(n)
        for i in range(len(n)):
            if n[i] != '0':
                if i == 0:
                    print(-1)
                    return
                else:
                    print(i)
                    return
        print(-1)

if __name__ == "__main__":
    main()
