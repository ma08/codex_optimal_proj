

def is_valid(num):
    """
    """
    if len(num) != 6 or any([x == '0' for x in num]):
        return False
    if len(set(num)) != 6:
        return False
    for i in num:
        if int(num) % int(i) != 0:
            return False
    return True

def main():
    """
    """
    l, h = [int(x) for x in input().split()]
    count = 0
    for i in range(l, h + 1):
        if is_valid(str(i)):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
