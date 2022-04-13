

import fileinput

def is_valid_combination(combination):
    combination = [int(i) for i in list(combination)]
    if len(combination) != 6:
        return False
    if len(set(combination)) != 6:
        return False
    for i in combination:
        if combination[0] % i != 0:
            return False
    return True

def main():
    for line in fileinput.input():
        L, H = line.split()
        L = int(L)
        H = int(H)
        count = 0
        for i in range(L, H + 1):
            if is_valid_combination(str(i)):
                count += 1
        print(count)

if __name__ == '__main__':
    main()
