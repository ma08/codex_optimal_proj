

def main():
    s = input().split()
    
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]: # if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")
    
    
if __name__ == '__main__':
    main()
