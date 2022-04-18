

def main():
    input = [int(x) for x in raw_input().split()]
    for i, num in enumerate(input):
        if i == 0:
            print(1-num, end=" ")
        elif i == 1:
            print(1-num, end=" ")
        elif i == 2:
            print(2-num, end=" ")
        elif i == 3:
            print(2-num, end=" ")
        elif i == 4:
            print(2-num, end=" ")
        else:
            print(8-num)

main()
