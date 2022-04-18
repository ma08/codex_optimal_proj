

def main():
    k = int(input())
    if k == 1:
        print(1, 0)
        return
    bar = 1
    brk = 0
    while bar < k:
        bar *= 2
        brk += 1
    print(bar, brk)

if __name__ == '__main__':
    main()
