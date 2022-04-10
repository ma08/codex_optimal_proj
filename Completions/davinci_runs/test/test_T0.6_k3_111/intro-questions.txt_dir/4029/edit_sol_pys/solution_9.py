

def main():
    n = int(input())
    if n % 25 == 0:  # if the number is divisible by 25, then it is divisible by 5 and 5, so print 0
        print(0)
    else:
        n = str(n)  # convert the number to string
        n = n[::-1]  # reverse the string
        n = n.lstrip("0")  # remove the leading zeros
        if len(n) < 2:  # if the length of the string is less than 2, then print -1
            print(-1)
        else:
            count = 0
            while True:  # while loop to check if the number is divisible by 25
                if len(n) < 2:  # if the length of the string is less than 2
                    if int(n) % 25 == 0:  # if the number is divisible by 25
                        print(count)
                    else:  # if the number is not divisible by 25
                        print(-1)
                    break
                else:
                    if int(n[0]) % 5 == 0:  # if the first digit is divisible by 5
                        count += 1
                        n = n[1:]  # remove the first digit
                    else:  # if the first digit is not divisible by 5
                        n = n[1:]
                        count += 1


if __name__ == '__main__':
    main()
