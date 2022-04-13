

def main():
    k = int(input())
    if k == 1:
        print(1, 0)
        return
    bar = 1
    break_ = 1
    while bar < k:
        bar *= 2
        break_ += 1
    print(bar, break_)

if __name__ == '__main__':
    main()
