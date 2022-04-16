

def main():
    x, y, z = map(int, input().split())
    if x <= 4 and y <= 4 and z <= 4:
        print('Yes')
    elif x <= 8 and y <= 8 and z <= 8:
        print('Yes')
    elif x <= 12 and y <= 12:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
