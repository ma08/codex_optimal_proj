

def main():
    number = int(input())
    for i in range(number):
        number = input()
        if number[:3] == "555":
            print(1)
        else:
            print(0)

main()
