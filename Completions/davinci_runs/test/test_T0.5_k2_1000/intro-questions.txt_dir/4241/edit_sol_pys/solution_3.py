

def min_changes(s, t): # function to count minimum changes
    count = 0
    for i in range(len(t)):
        if s[i] != t[i]:
            count += 1
    return count

def main():
    s = input() # input first string 
    t = input() # input second string 
    print(min_changes(s, t)) # print the minimum changes

if __name__ == '__main__':
    main()
