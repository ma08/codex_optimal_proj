
def main():
    while True:
        try:
            words = list(set(input().split()))
            if len(words) == len(input().split()):
                print("yes")
            else:
                print("no")
        except EOFError:
            break


main()
