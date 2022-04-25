

def main():
    x = [int(i) for i in input().split()]
    if x[0] < x[1]:
        print('<')
    elif x[0] == x[1]:
        print('=')
    else:
        print('>')

if __name__ == '__main__':
    main()
