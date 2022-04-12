# https://open.kattis.com/problems/trik

def main():
    moves = input()
    cup = 1
    for i in moves:
        if i == "A":
            if cup == 1:
                cup = 2
            elif cup == 2:
                cup = 1
        elif i == "B":
            if cup == 2:
                cup = 3
            elif cup == 3:
                cup = 2
        elif i == "C":
            if cup == 1:
                cup = 3
            elif cup == 3:
                cup = 1
    print(cup)

if __name__ == '__main__':
    main()
