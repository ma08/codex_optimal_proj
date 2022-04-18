

def main():
    while True:
        try:
            words1 = list(set(input().split()))
            words2 = input().split()
            if len(words1) == len(words2):
                print("yes")
            else:
                print("no")
        except:
            break

main()
