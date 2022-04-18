

def main():
    number = int(input())
    if number % 4 == 0:
        if number % 100 != 0:
            print(1)
        else:
            if number % 400 == 0:
                print(1)
            else:
                print(0)
    else:
        print(0)    

main()
