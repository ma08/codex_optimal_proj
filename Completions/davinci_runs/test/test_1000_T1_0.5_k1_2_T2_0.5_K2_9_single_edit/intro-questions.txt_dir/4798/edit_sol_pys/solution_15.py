

def main():
    n = input()
    n = n.split('-') #split the string by '-'
    for i in n:
        print(i[0], end="")
    print()

main()
