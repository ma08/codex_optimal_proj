

def main():
    l, h = [int(x) for x in input().split()] # input is a string
    count = 0
    for i in range(l, h + 1): # range is a function
        if is_valid(str(i)): # str is a function
            count += 1

    print(count)

def is_valid(c):
    if len(c) != 6 or any([x == '0' for x in c]): # len is a function
        return False
    if len(set(c)) != 6:
        return False
    for i in c:
        if int(c) % int(i) != 0: # int is a function
            return False
    return True

if __name__ == '__main__':
    main()
