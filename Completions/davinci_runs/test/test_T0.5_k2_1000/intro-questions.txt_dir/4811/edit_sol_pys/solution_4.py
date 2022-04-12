

def main():
    k = int(input())
    if k == 1:
        print(1, 0)
        return
    b = 1
    br = 0
    while b < k:
        b *= 2
        br += 1
    print(b, br) 

if __name__ == '__main__':
    main()
