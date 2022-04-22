

import sys

def is_lucky_number(number, k):
    if len(number) == k:
        return True
    else:
        for i in range(len(number)):
            if number[i] == "4" or number[i] == "7":
                new_number = number[:i] + number[i+1:]
                if is_lucky_number(new_number, k):
                    return True
        return False    

def main():
    number, k = sys.stdin.readline().strip().split()
    if is_lucky_number(number, int(k)):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
