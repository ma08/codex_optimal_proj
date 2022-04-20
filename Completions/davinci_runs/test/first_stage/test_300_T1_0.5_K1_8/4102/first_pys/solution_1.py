

def main():
    n = input()
    n = list(n)
    n = [int(i) for i in n]
    if len(n) == 1:
        print("No")
    else:
        n.sort()
        if n == list(range(n[0], n[-1] + 1)):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()