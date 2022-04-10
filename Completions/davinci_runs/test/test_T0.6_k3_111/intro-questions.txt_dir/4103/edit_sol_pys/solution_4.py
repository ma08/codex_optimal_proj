

def main():
    """
    The code is written in Python 3.6.1. To run the code, please use the below command in the terminal:

    python3 solution.py < input.txt

    """

    n, b, a = map(int, input().split())
    s = list(map(int, input().split()))
    b_init = b
    a_init = a
    count = 0
    while a > 0:
        if s[count] == 1:
            if b < b_init:
                b += 1
            else:
                a -= 1
        else:
            a -= 1
        count += 1
    while b > 0:
        if s[count] == 1:
            if b < b_init:
                b += 1
            else:
                a -= 1
        else:
            b -= 1
        count += 1
    print(count - 1)

if __name__ == "__main__":
    main()
