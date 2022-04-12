

def main():
    number = input()
    if number[:3] == "555" and len(number) == 10:  # noqa
        print(1)
    else:
        print(0)

main()
