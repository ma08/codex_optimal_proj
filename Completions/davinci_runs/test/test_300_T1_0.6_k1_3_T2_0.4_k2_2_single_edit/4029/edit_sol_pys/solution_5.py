

n = int(input())

def mod25(n):
    if n % 25 == 0:
        return True
    else:
        return False

def swap_adjacent(num):
    num = str(num)
    num1 = num[0]
    num2 = num[1]
    num = num2 + num1 + num[2:]
    return num

def main():
    num = str(n)
    counter = 0
    while(len(num) > 2):
        if mod25(int(num)):
            break
        else:
            num = swap_adjacent(num)
            counter += 1
    if mod25(int(n)):
        print(counter)
    else:
        print(-1)

main()
