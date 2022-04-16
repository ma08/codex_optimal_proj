

#!/usr/bin/env python3

def main():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    seen = set()
    for word in words:
        if word in seen:
            print("No")
            return
        seen.add(word)
    print("Yes")

if __name__ == "__main__":
    main()
