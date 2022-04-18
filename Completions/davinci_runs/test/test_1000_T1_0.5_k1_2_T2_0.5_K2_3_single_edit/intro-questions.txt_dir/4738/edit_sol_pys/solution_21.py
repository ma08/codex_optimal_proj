
def main():
    string = input()
    l = 1
    while l <= len(string):
        if string[:l] * (len(string) // l) == string:
            print(l)
            break
        l += 1

if __name__ == "__main__":
    main()
