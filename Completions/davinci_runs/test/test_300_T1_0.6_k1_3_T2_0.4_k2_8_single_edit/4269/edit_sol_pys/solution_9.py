

def main():
    s = input()  # input
    
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")  # output
    else:
        print("Good")  # output
    
    
if __name__ == '__main__':
    main()
