
def main():
    num = input()
    if len(num) > 1:
        for i in range(1, len(num)):
            if num[i] > num[i-1]:
                print('Yes')
                return
        print('No')
    else:
        print('Yes')

main()
