

def main():
    name = input()
    name = name.split('_')
    for i in name:
        print(i[0], end="")
    print()

main()
