

def main():
    num = list(map(int, input().split()))
    num.sort()
    if num[1] - num[0] == num[2] - num[1]:
        print(num[2] + num[1] - num[0])
    else:
        print(num[1] + num[1] - num[0])

main()
