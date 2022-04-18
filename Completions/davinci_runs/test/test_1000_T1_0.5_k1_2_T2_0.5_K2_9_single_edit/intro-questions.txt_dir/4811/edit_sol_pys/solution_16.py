
def main():
    k = int(input())
    if k == 1:
        print(1, 0)
        return
    bar = 1
    breaks = 0
    while bar < k:
        bar *= 2
        breaks += 1
    print(bar, breaks)

if __name__ == '__main__':
    main()
