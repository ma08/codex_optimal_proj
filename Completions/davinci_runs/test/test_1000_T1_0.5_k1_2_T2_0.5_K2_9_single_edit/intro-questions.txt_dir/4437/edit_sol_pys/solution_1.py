

def main():
    n = int(input())
    s = input()

    if s.count('a') % 2 == 1:
        print(1)
        print(s.replace('a', 'b', 1))
    elif s.count('b') % 2 == 1:
        print(1)
        print(s.replace('b', 'a', 1))
    else:
        print(0)
        print(s)

if __name__ == '__main__':
    main()
