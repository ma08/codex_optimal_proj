

def main():
    while True:
        try:
            words = list(set(input().split())) #list of unique words
            if len(words) == len(input().split()):
                print("yes")
            else:
                print("no")
        except:
            break

main()
