

def main():
    """
    """
    l, h = [int(x) for x in input().split()]
    count = 0
    for i in range(l, h + 1):
        if is_valid(str(i)):
            count += 1

    print(count)

def is_valid(c):
    """
    """
    if len(c) != 6 or any([x == '0' for x in c]):  # check if the length is 6 and if there are any zeros
        return False
    if len(set(c)) != 6:  # check if there are any repeating digits
        return False
    for i in c:
        if int(c) % int(i) != 0:
            return False
    return True

if __name__ == '__main__':
    main()
