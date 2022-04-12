

def main():
    l, h = [int(x) for x in input().split()]  # l = lower bound, h = higher bound
    count = 0
    for i in range(l, h + 1):
        if is_valid(str(i)):  # check if the number is valid
            count += 1

    print(count)

def is_valid(c):
    if len(c) != 6 or any([x == '0' for x in c]):  # check for length and if there are zeros
        return False
    if len(set(c)) != 6:  # check if all the digits are unique
        return False
    for i in c:  # check if the number is divisible by each digit
        if int(c) % int(i) != 0:
            return False
    return True

if __name__ == '__main__':
    main()
