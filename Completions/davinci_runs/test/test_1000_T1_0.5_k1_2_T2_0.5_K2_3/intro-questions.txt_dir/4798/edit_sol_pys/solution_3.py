

def main():
    names = input()
    names = names.split('-')
    for i in names:
        print(i[0], end = "")
    print("")

main()
