

def main():
    while True:
        try:
            words = list(set(input().split())) # convert to a set, then back to a list
            if len(words) == len(input().split()): # check if the length of the list is the same as the length of the input
                print("yes")
            else:
                print("no")
        except:
            break

main()
