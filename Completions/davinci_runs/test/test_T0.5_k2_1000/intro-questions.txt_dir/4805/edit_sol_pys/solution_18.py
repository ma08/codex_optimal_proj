def main():
    while True:
        try:
            words = input().split()
            if len(words) == len(set(words)):
                print("yes")
            else:
                print("no")
        except:
            break


main()
