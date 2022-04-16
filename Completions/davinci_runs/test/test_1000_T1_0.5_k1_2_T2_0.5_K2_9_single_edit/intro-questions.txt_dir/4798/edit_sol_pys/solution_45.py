

def main():
    n = input("Enter the number")
    n = n.split('-')
    for i in n:
        print(i[0], end="")
    print()

main()
