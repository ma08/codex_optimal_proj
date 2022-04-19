

def main():
    # Read input
    x, a = [int(i) for i in input().split()] # x = 5, a = 6

    if x < a: # 5 < 6
        print(0) # 0
    else: # 5 >= 6
        print(10) # 10

if __name__ == '__main__':
    main()
