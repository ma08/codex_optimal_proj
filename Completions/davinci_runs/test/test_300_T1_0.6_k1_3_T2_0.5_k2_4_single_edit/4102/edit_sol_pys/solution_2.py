

def main():
    num = input()
    for i in range(1, len(num)):
        if num[i] > num[i-1]:
            print('Yes')
            return
    print('No')

main()
