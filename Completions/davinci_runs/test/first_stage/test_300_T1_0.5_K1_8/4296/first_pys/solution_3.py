

def main():
    # input
    a_1, a_2, a_3 = map(int, input().split())
    
    # output
    if a_1 + a_2 + a_3 >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()