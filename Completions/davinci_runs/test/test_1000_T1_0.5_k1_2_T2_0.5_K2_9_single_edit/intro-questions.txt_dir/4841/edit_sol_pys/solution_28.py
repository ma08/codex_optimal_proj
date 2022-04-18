

def f(a):
    if a == 'mumble':
        return True
    elif int(a) == i+1:
        return True
    else:
        return False


def main():
    n = int(input())
    a = input().split()

    if len(a) != n:
        print('something is fishy')
    else:
        for i in range(len(a)):
            if f(a[i]):
                continue
            else:
                print('something is fishy')
                break
        else:
            print('makes sense')


if __name__ == '__main__':
    main()
