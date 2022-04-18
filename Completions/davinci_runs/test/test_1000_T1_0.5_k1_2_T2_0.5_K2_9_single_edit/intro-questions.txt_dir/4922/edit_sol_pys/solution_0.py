

def main():
    m, n = map(int, input().split()) # split string into a list
    if m < 8: # if m is less than 8
        print("unsatisfactory")
    else: # if m is greater than or equal to 8
        print("satisfactory")

if __name__ == "__main__":
    main()
