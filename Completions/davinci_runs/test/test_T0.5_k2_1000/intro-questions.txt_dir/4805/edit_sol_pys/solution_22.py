
def main():
    while True:
        try:
            words = list(set(input().split())) # remove duplicate words
            if len(words) == len(input().split()): # check if two lists have same length
                print("yes")
            else:
                print("no")
        except:
            break
main()
