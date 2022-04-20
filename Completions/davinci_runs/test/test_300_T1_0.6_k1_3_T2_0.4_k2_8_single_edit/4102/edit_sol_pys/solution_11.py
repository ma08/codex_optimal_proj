

def main():
    num = list(input())
    if len(num) > 1:
        for i in range(1, len(num)):
            if num[i] > num[i-1]:
                print('yes')
                return
        print('no')
    else:
        print('yes')

main()
