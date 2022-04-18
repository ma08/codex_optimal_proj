
import sys

num1 = sys.stdin.readline().rstrip()
num2 = sys.stdin.readline().rstrip()

if len(num1) > len(num2):
    print("GREATER")
elif len(num1) < len(num2):
    print("LESS")
else:
    for i in range(len(num1)):
        if int(num1[i]) > int(num2[i]):
            print("GREATER")
            break
        elif int(num1[i]) < int(num2[i]):
            print("LESS")
            break
        else:
            if i == len(num1)-1:
                print("EQUAL")

'''
def main(args):
    num = int(args[1])

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

if __name__ == '__main__':
    main(sys.argv)
'''
