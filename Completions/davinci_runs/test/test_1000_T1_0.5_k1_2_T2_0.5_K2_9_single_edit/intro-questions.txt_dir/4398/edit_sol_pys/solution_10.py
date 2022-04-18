

def main():
    n = int(input())
    s = list(input())
    t = list(input())
    res = ''
    for i in range(n):
        res += s.pop(0)
        res += t.pop(0)
    print(res)

if __name__ == '__main__':
    main()
