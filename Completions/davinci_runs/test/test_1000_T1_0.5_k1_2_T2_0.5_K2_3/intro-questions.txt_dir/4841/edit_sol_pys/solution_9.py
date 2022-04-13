

def main():
    n = int(input())
    bytes = input().split()
    for i in range(n):
        if bytes[i] != 'mumble' and int(bytes[i]) != i + 1:
            print('something is fishy')
            break
    else:
        print('makes sense')


if __name__ == '__main__':
    main()
