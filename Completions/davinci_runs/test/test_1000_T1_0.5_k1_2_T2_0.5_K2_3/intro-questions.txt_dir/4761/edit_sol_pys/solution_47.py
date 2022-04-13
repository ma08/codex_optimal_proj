

def main():
    """
    """
    l, h = [int(i) for i in input().split()]
    count = 0
    for i in range(l, h+1):
        if is_valid(str(i)) is True:
            count += 1

    print(count)

def is_valid(number):
    """
    """
    if len(number) != 6 or any([x == '0' for x in number]) or len(set(number)) != 6:
        return False

    for i in number:
        if int(number) % int(i) != 0:
            return False
    return True

if __name__ == '__main__':
    main()
