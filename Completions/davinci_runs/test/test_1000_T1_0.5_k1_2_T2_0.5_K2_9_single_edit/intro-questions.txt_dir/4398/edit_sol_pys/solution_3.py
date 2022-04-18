

def main():
    n = int(input())
    s = input()
    t = input()
    res = ''
    for i in range(n * 2):
        if i % 2 == 0:
            res += s[i // 2]
        else:
            res += t[i // 2]
    print(res)

if __name__ == '__main__':
    main()
