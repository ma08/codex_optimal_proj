#!/usr/bin/env python3

def main():
    phrase = input() 
    words = phrase.split() 
    seen = set()
    for word in words: 
        if word in seen: 
            print("no") 
            return 
        seen.add(word)
    print("yes")

if __name__ == "__main__":
    main()
