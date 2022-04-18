

def main():
    l_value, r_value = map(int, input().split())
    if l_value == 0 and r_value == 0:
        print("Not a moose")
    else:
        if l_value == r_value:
            print("Even {}".format(2*l_value))
        else:
            print("Odd {}".format(2*max(l_value, r_value)))

if __name__ == "__main__":
    main()
