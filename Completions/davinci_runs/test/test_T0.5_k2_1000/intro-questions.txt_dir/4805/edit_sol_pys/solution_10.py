
def main():
    while True:
        try:
            words = list(set(raw_input().split()))
            if len(words) == len(raw_input().split()):
                print("yes")
            else:
                print("no")
        except:
            break

main()
