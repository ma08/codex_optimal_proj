

def main():
    """main function"""
    num = list(map(int, input().split())) #list(map(int, input().split()))
    num.sort()
    if num[1] - num[0] == num[2] - num[1]:
        print(num[2] + num[1] - num[0]) #print(num[2] + num[1] - num[0])
    else:
        print(num[1] + num[2] - num[0]) #print(num[1] + num[2] - num[0])

main() #main()
