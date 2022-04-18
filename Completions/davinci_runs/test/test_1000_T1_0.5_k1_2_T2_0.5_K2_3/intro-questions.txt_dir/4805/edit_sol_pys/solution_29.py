

def main():
    while True:
        try:
            words = set(input().split())
            if len(words) == len(set(input().split())):
                print("yes")
            else:
                print("no")
        except:
            break


main()
