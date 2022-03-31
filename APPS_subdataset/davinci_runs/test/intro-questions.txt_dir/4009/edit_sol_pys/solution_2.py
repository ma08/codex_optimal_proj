

def main():
    n, x = map(int, input().split())
    nums = input()
    if nums[0] == '0':
        print(1)
    else:
        for i in range(x, n):
            if nums[i] == '0':
                print(1)
                break
        else:
            print(0)

if __name__ == '__main__':
    main()
