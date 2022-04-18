
def main():
    while True:
        try:
            words = set(input().split())
            if len(words) == len(input().split()):
                print("yes")
            else:
                print("no")
        except:
            break

main()
