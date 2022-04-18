

def main():
    n = int(input())
    s = input()
    t = input()
    res = []
    for i in range(n):
        res.append(s[i])
        res.append(t[i])
    print(''.join(res))

if __name__ == '__main__':
    main()
