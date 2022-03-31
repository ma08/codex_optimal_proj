

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        n = str(n)
        n = n[::-1]
        n = n.lstrip("0")
        if len(n) < 2:
            print(-1)
        else:
            count = 0
            while True:
                if len(n) < 2:
                    if int(n) % 25 == 0:
                        print(count)
                    else:
                        print(-1)
                    break
                else:
                    if int(n[0]) % 5 == 0:
                        count += 1
                        n = n[1:]
                    else:
                        n = n[1:]
                        count += 1


if __name__ == '__main__':
    main()