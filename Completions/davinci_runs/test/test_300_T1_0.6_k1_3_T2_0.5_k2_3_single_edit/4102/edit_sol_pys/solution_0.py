

def main():
    num = input()  # get input
    if len(num) > 1:  # if the number has more than one digit
        for i in range(1, len(num)):  # loop through the number
            if num[i] > num[i-1]:  # if the current digit is greater than the previous digit
                print('Yes')
                return
        print('No')
    else:  # if the number has only one digit
        print('Yes')

main()
