

def main():
    s = input() # s = "abcde"
    t = input() # t = "abcde"

    count = 0
    for i in range(len(t)): # i = 0, 1, 2, 3, 4
        if s[i] != t[i]: # s[0] != t[0]
            count += 1 # count = 1

    print(count) # print(1)

if __name__ == '__main__':
    main()
