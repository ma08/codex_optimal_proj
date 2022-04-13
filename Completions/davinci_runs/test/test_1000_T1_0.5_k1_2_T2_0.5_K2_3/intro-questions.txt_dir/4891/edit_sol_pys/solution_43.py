

def main():
    nums = [int(x) for x in input().split()]
    for i, num in enumerate(nums):
        if i == 0:
            print(2-num, end=" ")
        elif i == 1:
            print(3-num, end=" ")
        elif i == 2:
            print(3-num, end=" ")
        elif i == 3:
            print(4-num, end=" ")
        elif i == 4:
            print(2-num, end=" ")
        else:
            print(9-num)

main()
